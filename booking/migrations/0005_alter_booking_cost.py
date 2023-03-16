# Generated by Django 4.1.7 on 2023-03-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_cost_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=32),
        ),
    ]
