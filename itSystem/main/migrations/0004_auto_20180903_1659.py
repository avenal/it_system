# Generated by Django 2.1 on 2018-09-03 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180903_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
