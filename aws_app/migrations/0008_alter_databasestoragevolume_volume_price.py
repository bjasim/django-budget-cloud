# Generated by Django 4.2 on 2024-02-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws_app', '0007_remove_databasestoragevolume_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databasestoragevolume',
            name='volume_price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
    ]
