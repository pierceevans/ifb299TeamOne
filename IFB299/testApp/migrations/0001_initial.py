# Generated by Django 2.1.1 on 2018-09-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(max_length=25)),
                ('Customer_Phone', models.CharField(max_length=30)),
                ('Customer_Address', models.CharField(max_length=35)),
                ('Customer_Occupation', models.CharField(max_length=20)),
                ('Customer_Birthday', models.DateField()),
                ('Customer_Gender', models.CharField(max_length=1)),
            ],
        ),
    ]
