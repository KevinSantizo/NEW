# Generated by Django 2.2.5 on 2019-10-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20191024_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Ocupada'), ('2', 'Mantenimiento')], default='1', max_length=1),
        ),
    ]