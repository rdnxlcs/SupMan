# Generated by Django 4.1.2 on 2024-03-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0002_remove_moves_date_items_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]