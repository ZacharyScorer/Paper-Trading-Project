# Generated by Django 3.0.7 on 2020-07-25 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper_trade', '0002_auto_20200724_2036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaperTradeTickers',
            new_name='PaperTradeTicker',
        ),
    ]