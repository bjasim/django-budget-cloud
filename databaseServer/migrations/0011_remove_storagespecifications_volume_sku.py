# Generated by Django 5.0.2 on 2024-02-29 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseServer', '0010_storagespecifications_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storagespecifications',
            name='volume_sku',
        ),
    ]