# Generated by Django 3.0.6 on 2020-07-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle_manager', '0010_auto_20200701_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battleplan',
            name='additional_rules',
            field=models.ManyToManyField(blank=True, to='battle_manager.AdditionalRule'),
        ),
    ]
