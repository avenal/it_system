# Generated by Django 2.1 on 2018-09-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realizations', '0002_auto_20180904_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realization',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
