# Generated by Django 2.2.4 on 2019-08-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_merge_20190820_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='amount_of_asset_change',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='john_bur_term',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='rate_of_return',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='stock_name',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='total_assets',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='trade_numbers',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
