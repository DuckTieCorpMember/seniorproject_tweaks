# Generated by Django 2.2.2 on 2019-06-25 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_faces_visitors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitors',
            name='folderLocation',
        ),
        migrations.RemoveField(
            model_name='visitors',
            name='numberPhotos',
        ),
    ]