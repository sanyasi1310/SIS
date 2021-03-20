# Generated by Django 3.1.3 on 2020-11-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('faculty', models.CharField(max_length=200)),
                ('credits', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=200, primary_key=True, serialize=False)),
                ('courseId', models.CharField(max_length=200)),
                ('studentId', models.CharField(max_length=200)),
                ('totalGrade', models.CharField(max_length=200)),
                ('fees', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialServices',
            fields=[
                ('id', models.AutoField(auto_created=True, max_length=200, primary_key=True, serialize=False)),
                ('studentId', models.CharField(max_length=200)),
                ('totalFee', models.CharField(max_length=200)),
                ('unpaid', models.CharField(max_length=200)),
                ('paid', models.CharField(max_length=200)),
                ('due', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HelpDesk',
            fields=[
                ('id', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('studentId', models.CharField(max_length=200)),
                ('problemCategory', models.CharField(max_length=200)),
                ('subcategory', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('explanation', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('studentId', models.CharField(max_length=200)),
                ('startDate', models.CharField(max_length=200)),
                ('endDate', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
