# Generated by Django 5.0.6 on 2024-06-15 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_credintial', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
