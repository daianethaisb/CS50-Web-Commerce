# Generated by Django 4.2.4 on 2023-09-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auction_auction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]