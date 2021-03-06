# Generated by Django 2.1 on 2018-09-09 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=128)),
                ('text', models.TextField(max_length=256)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('done', models.BooleanField(default=0)),
            ],
        ),
    ]
