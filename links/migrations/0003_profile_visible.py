# Generated by Django 3.2.13 on 2022-04-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
