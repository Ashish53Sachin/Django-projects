# Generated by Django 4.1.7 on 2023-04-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'others')], default=1, max_length=1),
        ),
    ]
