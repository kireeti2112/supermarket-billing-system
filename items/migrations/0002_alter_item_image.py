# Generated by Django 5.1.4 on 2024-12-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/media/'),
        ),
    ]
