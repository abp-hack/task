# Generated by Django 4.1.7 on 2023-03-13 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('sum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_a', models.IntegerField()),
                ('field_b', models.ImageField(upload_to='')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.summodel')),
            ],
        ),
    ]