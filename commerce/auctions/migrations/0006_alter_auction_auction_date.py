# Generated by Django 4.2.4 on 2023-09-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auction_buy_date_auction_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_date',
            field=models.DateTimeField(null=True),
        ),
    ]