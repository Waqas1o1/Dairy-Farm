# Generated by Django 3.1.7 on 2021-03-03 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mstock',
            old_name='mStock_product_animal',
            new_name='mStock_product_detail',
        ),
        migrations.RemoveField(
            model_name='mproduct',
            name='mProduct_animal',
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]