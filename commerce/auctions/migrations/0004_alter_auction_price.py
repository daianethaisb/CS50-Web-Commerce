# Generated by Django 4.2.4 on 2023-09-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_bid_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
