# Generated by Django 3.1.5 on 2022-04-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ph_num', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
    ]
