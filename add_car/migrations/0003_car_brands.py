# Generated by Django 5.0.6 on 2024-06-16 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_car', '0002_alter_car_car_img'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brands',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='brands.brands'),
        ),
    ]
