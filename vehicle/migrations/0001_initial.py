# Generated by Django 3.0.8 on 2020-07-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('Location', models.TextField(max_length=100)),
                ('CameraID', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CarRTO',
            fields=[
                ('Brand', models.CharField(max_length=20)),
                ('Owner', models.CharField(max_length=30)),
                ('DateRegistered', models.DateTimeField(auto_now_add=True)),
                ('CarModel', models.CharField(max_length=20)),
                ('PlateNumber', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CarSurveillance',
            fields=[
                ('LastSeen', models.DateTimeField(auto_now=True)),
                ('Color', models.CharField(max_length=10)),
                ('CarModel', models.CharField(max_length=20)),
                ('FirstSeen', models.DateTimeField(auto_now_add=True)),
                ('PlateNumber', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Brand', models.CharField(max_length=20)),
            ],
        ),
    ]
