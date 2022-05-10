# Generated by Django 3.1.5 on 2022-04-23 06:18

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
