# Generated by Django 2.1 on 2018-09-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contactmodel_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]