# Generated by Django 5.1.1 on 2024-09-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_profile_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='photo_default.png', upload_to='profile_pictures'),
        ),
    ]
