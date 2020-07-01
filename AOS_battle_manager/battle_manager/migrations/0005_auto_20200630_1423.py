# Generated by Django 3.0.6 on 2020-06-30 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battle_manager', '0004_battleplan_battle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='additionalrule',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battleplan',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='commandability',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='realmfeature',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spell',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='terrainfeature',
            name='source_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='additionalrule',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
        migrations.AddField(
            model_name='battleplan',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
        migrations.AddField(
            model_name='commandability',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
        migrations.AddField(
            model_name='realmfeature',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
        migrations.AddField(
            model_name='spell',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
        migrations.AddField(
            model_name='terrainfeature',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='battle_manager.Source'),
        ),
    ]
