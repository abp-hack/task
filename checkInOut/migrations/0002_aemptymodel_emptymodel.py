# Generated by Django 4.1.7 on 2023-03-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkInOut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AEmptyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EmptyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]