# Generated by Django 2.1.3 on 2018-12-03 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0013_mproductsell_buyer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mproductsell',
            name='buyer',
        ),
        migrations.AddField(
            model_name='mproductsell',
            name='mProductSell_amount',
            field=models.FloatField(default=0),
        ),
    ]
