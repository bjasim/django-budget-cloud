# Generated by Django 5.0.2 on 2024-03-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseServer', '0009_remove_computespecifications_price_per_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computespecifications',
            name='price_monthly',
            field=models.CharField(default='0.0', max_length=50),
        ),
        migrations.AddField(
            model_name='databasespecifications',
            name='price_monthly',
            field=models.CharField(default='0.0', max_length=50),
        ),
        migrations.AddField(
            model_name='networkingspecifications',
            name='price_monthly',
            field=models.CharField(default='0.0', max_length=50),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='price_monthly',
            field=models.CharField(default='0.0', max_length=50),
        ),
    ]