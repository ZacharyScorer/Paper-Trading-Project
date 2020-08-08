# Generated by Django 3.0.7 on 2020-07-25 04:37

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_trade', '0004_papertrade_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papertrade',
            name='money',
            field=models.FloatField(default=5000.0, verbose_name=django.contrib.auth.models.User),
        ),
    ]