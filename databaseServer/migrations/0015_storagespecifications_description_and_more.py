# Generated by Django 5.0.2 on 2024-02-29 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseServer', '0014_databasespecifications_cpu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagespecifications',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='durability',
            field=models.CharField(default='No durability provided.', max_length=50),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='service_code',
            field=models.CharField(default='No code provided.', max_length=50),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='storage_class',
            field=models.CharField(default='No class provided.', max_length=50),
        ),
        migrations.AddField(
            model_name='storagespecifications',
            name='volume_type',
            field=models.CharField(default='No type provided.', max_length=50),
        ),
    ]