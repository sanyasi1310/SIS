# Generated by Django 3.1.3 on 2020-11-28 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MTU', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='startDate',
        ),
    ]
