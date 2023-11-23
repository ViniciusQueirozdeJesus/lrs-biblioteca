# Generated by Django 4.2.5 on 2023-11-23 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile_pictures/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])]),
        ),
    ]
