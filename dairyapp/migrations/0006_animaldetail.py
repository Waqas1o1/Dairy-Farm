# Generated by Django 3.1.7 on 2021-03-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0005_mstock_mstock_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='animalDetail',
            fields=[
                ('animalDetail_id', models.AutoField(primary_key=True, serialize=False)),
                ('animalDetail_name', models.CharField(max_length=50)),
                ('animalDetail_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]