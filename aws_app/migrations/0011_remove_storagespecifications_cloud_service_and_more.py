# Generated by Django 4.2 on 2024-02-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws_app', '0010_remove_databasespecifications_cloud_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storagespecifications',
            name='cloud_service',
        ),
        migrations.RemoveField(
            model_name='storagespecifications',
            name='redundancy',
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='instance_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='sku',
            field=models.CharField(default='SKU not provided', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='volume_type',
            field=models.CharField(default='No type provided.', max_length=50),
        ),
    ]