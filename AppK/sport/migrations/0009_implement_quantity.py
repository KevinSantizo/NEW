# Generated by Django 2.2.5 on 2019-11-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0008_implement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='implement',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
