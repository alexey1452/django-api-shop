# Generated by Django 3.0.3 on 2020-03-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_productsimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsimages',
            name='mime_type',
        ),
        migrations.RemoveField(
            model_name='productsimages',
            name='name',
        ),
        migrations.RemoveField(
            model_name='productsimages',
            name='size',
        ),
        migrations.AddField(
            model_name='productsimages',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
    ]
