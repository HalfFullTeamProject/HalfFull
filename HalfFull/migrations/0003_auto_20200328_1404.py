# Generated by Django 2.2.3 on 2020-03-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HalfFull', '0002_auto_20200328_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('drinks', models.IntegerField(default=0)),
                ('atmosphere', models.IntegerField(default=0)),
                ('service', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, upload_to='pub_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]