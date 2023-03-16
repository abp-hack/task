# Generated by Django 4.1.7 on 2023-03-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_sums_field_b'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='HotelNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='Номер')),
                ('level', models.IntegerField(verbose_name='Этаж')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='application.hotel', verbose_name='Отель')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='application.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Номер отеля',
                'verbose_name_plural': 'Номера отелей',
            },
        ),
    ]