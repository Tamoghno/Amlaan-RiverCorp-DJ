# Generated by Django 3.1.5 on 2022-04-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0002_auto_20220423_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]