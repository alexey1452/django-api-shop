# Generated by Django 3.0.3 on 2020-04-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_profile_confirmation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
