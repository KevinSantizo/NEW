# Generated by Django 2.2.5 on 2019-11-05 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191024_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='town',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='towns', to='user.Department'),
        ),
    ]
