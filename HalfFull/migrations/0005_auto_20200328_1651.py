# Generated by Django 2.2.3 on 2020-03-28 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HalfFull', '0004_auto_20200328_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
