# Generated by Django 2.0.7 on 2019-03-31 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_visitors'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthSensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensortype', models.CharField(max_length=50)),
                ('data', models.FloatField()),
                ('date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='mSensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensortype', models.CharField(max_length=50)),
                ('data', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
                ('owner_id', models.IntegerField()),
            ],
        ),
    ]