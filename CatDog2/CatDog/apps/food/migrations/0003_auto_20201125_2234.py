# Generated by Django 2.1.7 on 2020-11-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20201125_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to='food_images'),
        ),
    ]
