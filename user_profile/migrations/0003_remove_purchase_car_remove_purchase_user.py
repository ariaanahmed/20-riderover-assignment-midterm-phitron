# Generated by Django 5.0.6 on 2024-06-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_purchase_car_alter_purchase_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='car',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
    ]
