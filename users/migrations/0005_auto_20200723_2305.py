# Generated by Django 3.0.7 on 2020-07-24 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20200723_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
            ],
        ),
        migrations.RenameModel(
            old_name='Watchlist',
            new_name='Portfolio',
        ),
        migrations.DeleteModel(
            name='WatchlistTicker',
        ),
        migrations.AddField(
            model_name='portfolioticker',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Portfolio'),
        ),
    ]
