# Generated by Django 4.1.2 on 2024-03-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0004_alter_moves_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='rule',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moves',
            name='item_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moves',
            name='point_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moves',
            name='type',
            field=models.BooleanField(),
        ),
    ]