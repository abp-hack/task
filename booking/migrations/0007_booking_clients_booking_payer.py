# Generated by Django 4.1.7 on 2023-03-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_client_guest_alter_booking_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='clients',
            field=models.ManyToManyField(null=True, to='booking.guest', verbose_name='Проживающие'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.client', verbose_name='Плательщик'),
        ),
    ]
