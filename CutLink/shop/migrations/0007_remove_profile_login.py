# Generated by Django 5.1.1 on 2024-09-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_profile_url_delete_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='login',
        ),
    ]