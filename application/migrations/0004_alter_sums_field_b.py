# Generated by Django 4.1.7 on 2023-03-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_summodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sums',
            name='field_b',
            field=models.IntegerField(),
        ),
    ]
