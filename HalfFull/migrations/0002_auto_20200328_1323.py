# Generated by Django 2.2.3 on 2020-03-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HalfFull', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
