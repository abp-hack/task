# Generated by Django 4.1.7 on 2023-03-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата заезда'),
        ),
    ]
