# Generated by Django 3.0.6 on 2020-06-30 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battle_manager', '0006_auto_20200630_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realmfeature',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
    ]