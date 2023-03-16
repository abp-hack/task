# Generated by Django 4.1.7 on 2023-03-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_status_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hotelnumber',
            name='category',
            field=models.CharField(choices=[('Стандарт', 'Стандарт'), ('Люкс', 'Люкс'), ('Апартамент', 'Апартамент')], default='Стандарт', max_length=100, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='hotelnumber',
            name='how_many',
            field=models.IntegerField(default=2, verbose_name='Количество мест'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.region'),
        ),
    ]
