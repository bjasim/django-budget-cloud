# Generated by Django 4.2 on 2024-02-28 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws_app', '0013_alter_storagespecifications_storage_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storagespecifications',
            old_name='instance_price',
            new_name='price',
        ),
    ]
