# Generated by Django 3.1.3 on 2020-11-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTU', '0002_auto_20201128_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='event1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]