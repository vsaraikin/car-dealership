from decimal import Decimal
from celery import shared_task
from buyers.models import Buyers, BuyerOffer, BuyerHistory, BuyerStatistic
from dealers.models import Dealers, SupplierToDealer, Dealer, DealerPromotion, DealerToBuyer, DealerStatistic
from suppliers.models import Supplier, SupplierPromotion, SupplierStatistic


@shared_task
def dealer_to_buyer_task():
    disc = 0.9  # multiplied with buyer's amount

    """ Task for a customer buying a car from a dealer"""
    for buyer in Buyers.objects.all():
        # Check the balance for buying a car
        max_buyer_price = Decimal(buyer.balance.amount).quantize(Decimal('1.00')) * Decimal(disc).quantize(
            Decimal('1.00'))
        # Creating an Offer to buy a car
        BuyerOffer.objects.create(
            buyer=buyer,
            max_price=max_buyer_price,
            characteristics_of_car={
                'car_brand': buyer.characteristics_of_car.get('car_brand'),
                'car_model': buyer.characteristics_of_car.get('car_model'),
                'engine_type': buyer.characteristics_of_car.get('engine'),
                'transmission': buyer.characteristics_of_car.get('transmission'),
                'color': buyer.characteristics_of_car.get('color'),
            },
        )
    for offer in BuyerOffer.objects.exclude(active_status=False):
        car_buyer = offer.buyer

        suit_dealers_list = Dealer.objects.select_related('car').filter(
            car__car__car_brand__in=offer.characteristics_of_car.get('car_brand'),
            car__car__car_model__in=offer.characteristics_of_car.get('car_model'),
            car__car__engine_type__in=offer.characteristics_of_car.get('engine_type'),
            car__car__transmission__in=offer.characteristics_of_car.get('transmission'),
            car__car__color__in=offer.characteristics_of_car.get('color'),
        )

        preferred_prices = {}
        for suit_dealer in suit_dealers_list:  # Dealer garage loop
            preferred_prices[suit_dealer.dealer] = [suit_dealer, suit_dealer.price.amount]
            promo_car = DealerPromotion.objects.filter(dealership=suit_dealer.dealer,
                                                       car=suit_dealer).first()
            if promo_car:
                preferred_prices[suit_dealer.dealer].append(promo_car.discount)

        for deal, lst in preferred_prices.items():
            if len(lst) == 3:
                preferred_prices[deal].append((lst[1] * Decimal(str((100 - lst[2]) / 100))).quantize(Decimal('1.00')))

        # Finding the best price
        best_prices_list = []
        for deal, lst in preferred_prices.items():
            best_prices_list.append([deal, lst[0], lst[-1]])

        if best_prices_list:
            best_prices_list = min(best_prices_list, key=lambda x: x[-1])  # get car with minimal price
            current_dealer = best_prices_list[0]
            current_car = best_prices_list[1]
            current_price = best_prices_list[2]

            # Update Buyer's history
            BuyerHistory.objects.create(buyer=car_buyer, car=current_car, price=current_price)

            # Update history
            if not DealerToBuyer.objects.filter(dealer=current_dealer, buyer=car_buyer).first():
                DealerToBuyer.objects.create(
                    car=current_car, dealer=current_dealer, buyer=car_buyer,
                    price=current_price, car_count=1, total_sum=current_price)

            else:
                # Update history
                update_buyer_car = DealerToBuyer.objects.filter(dealer=current_dealer, buyer=car_buyer).get()
                update_buyer_car.car_count += 1
                update_buyer_car.total_sum.amount += current_price
                update_buyer_car.save()

            # Update balances of dealer and buyer
            car_buyer.balance.amount -= current_price
            car_buyer.save()

            current_dealer.balance.amount += current_price
            current_dealer.save()

            current_car.car_count -= 1
            current_car.save()

            if current_car.car_count == 0:
                Dealer.objects.filter(car=current_car.car, dealership=current_dealer).delete()

        offer.active_status = False
        offer.save()

        # Statistics of Buyer
        print(f"Statistics for Buyer {car_buyer.first_name} {car_buyer.last_name}")
        buyer_stat = BuyerStatistic.objects.filter(buyer_stats=car_buyer).first()

        if not buyer_stat:
            BuyerStatistic.objects.create(buyer_stats=car_buyer, total_cost=current_price, total_count=1)

        else:
            buyer_stat.total_spent_sum.amount += current_price
            buyer_stat.total_car_count += 1
            buyer_stat.save()

        # Statistics of Dealer
        dealer_stat = DealerStatistic.objects.filter(dealer_stats=current_dealer).first()

        dealer_stat.total_revenue_sum += current_price
        dealer_stat.total_spent_car_count += 1
        dealer_stat.save()


@shared_task
def supplier_to_dealer_task():
    purchase_price = 111000  # USD
    discount = 5  # 5%
    margin = Decimal(1.05)  # 5% margin
    current_count = 0
    max_discount = 10  # percentage amount
    amount_cars_for_discount = 1  # percentage amount

    """ Task for a dealer buying a car from a supplier """
    for dealer in Dealers.objects.all():
        preferred_cars = Supplier.objects.select_related('car').filter(
            car__car_brand__in=dealer.characteristics_of_car.get('car_brand'),
            car__car_model__in=dealer.characteristics_of_car.get('car_model'),
            car__engine_type__in=dealer.characteristics_of_car.get('engine_type'),
            car__transmission__in=dealer.characteristics_of_car.get('transmission'),
            car__color__in=dealer.characteristics_of_car.get('color'),
        )

        if preferred_cars:
            for pref_car in preferred_cars:
                # Find suitable car from Supplier
                suitable_supplier_cars = Supplier.objects.filter(car=pref_car.car)
                if suitable_supplier_cars:
                    preferred_prices = {}
                    car_and_price = []
                    for suitable_car in suitable_supplier_cars:
                        cars_count = SupplierToDealer.objects.filter(supplier=suitable_car.name, dealer=dealer).count()
                        preferred_prices[suitable_car.name.id] = [suitable_car, cars_count]

                    cars_promos = SupplierPromotion.objects.filter(car=pref_car)

                    # Check if promotions exist
                    if cars_promos:
                        car_to_promo = cars_promos[0]
                        preferred_prices[car_to_promo.supplier.id].append(car_to_promo.discount)
                        count_discount = int(car_to_promo.supplier.car_count) // amount_cars_for_discount

                        if count_discount > max_discount:
                            count_discount = max_discount

                    else:
                        count_discount = 0

                    # Discount calculation
                    for sup_id, lst in preferred_prices.items():
                        if len(lst) == 2:  # if random car-promo IS NOT available
                            car_and_price = (lst[0], (lst[0].price.amount * Decimal(
                                str((100 - count_discount) / 100))).quantize(Decimal('1.00')))

                        elif len(lst) == 3:  # if random car-promo IS available
                            car_and_price = (lst[0], (lst[0].price.amount * Decimal(
                                str((100 - lst[2] - count_discount) / 100))).quantize(Decimal('1.00')))

                    # Buying a car
                    current_car = car_and_price[0]
                    current_price = car_and_price[1]

                    # Generate random price margin to bought car to dealership garage.
                    current_new_price = (current_price * margin)

                    # Check dealership balance
                    if dealer.balance.amount >= current_price * current_count:
                        # Check a car to enter the Dealership
                        current_dealer_garage = [car.car for car in Dealer.objects.filter(dealer=dealer)]
                        if current_car not in current_dealer_garage:
                            Dealer.objects.create(car=current_car, dealer=dealer,
                                                  car_count=current_count, price=current_new_price)

                            DealerPromotion.objects.create(dealer=dealer, car=Dealer.objects.latest('id'),
                                                           discount=discount)

                        else:
                            update_dealer_car = Dealer.objects.filter(car=current_car, dealer=dealer).get()
                            update_dealer_car.car_count += current_count
                            update_dealer_car.save()

                        # Update number of Supplier's cars
                        current_car.name.car_count += current_count
                        current_car.name.save()

                    else:
                        dealer.balance.amount += purchase_price
                        dealer.save()

                    # Update dealer's balance
                    dealer.balance.amount -= current_price * current_count
                    dealer.save()

                # Adding to History
                SupplierToDealer.objects.create(car=current_car, supplier=current_car.name, dealer=dealer,
                                                price=current_price, car_count=current_count,
                                                total_cost=current_price * current_count, )

                # Statistics of Supplier
                supplier_stat = SupplierStatistic.objects.filter(supplier_stat=current_car.name).first()

                if not supplier_stat:
                    SupplierStatistic.objects.create(supplier_stat=current_car.name, revenue=current_price,
                                                     car_count=current_count)
                else:
                    supplier_stat.revenue.amount += current_price
                    supplier_stat.car_count += current_count
                    supplier_stat.save()

                # Statistics of Dealer
                dealer_stat = DealerStatistic.objects.filter(dealer_stats=dealer).first()

                if not dealer_stat:
                    DealerStatistic.objects.create(
                        dealer_stats=dealer, cost=current_price, revenue=0, total_bought_car_count=current_count,
                        total_sold_car_count=0,)
                else:
                    dealer_stat.revenue.amount += current_price
                    dealer_stat.total_bought_car_count += current_count
                    dealer_stat.save()
