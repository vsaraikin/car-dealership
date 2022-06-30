# Generated by Django 4.0.5 on 2022-06-30 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0001_initial'),
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerhistory',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dealers.dealer', verbose_name='Car bought'),
        ),
    ]