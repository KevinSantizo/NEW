# Generated by Django 2.2.6 on 2019-11-11 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0003_auto_20191108_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='sport.Field'),
        ),
    ]