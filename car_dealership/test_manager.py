import pytest

# collecting tests
from dealers.tests import test_api, test_index, test_api_dealers
from cars.tests import test_create_new_car

if __name__ == '__main__':
    pytest.main()
