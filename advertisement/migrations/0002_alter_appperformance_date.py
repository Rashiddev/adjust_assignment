# Generated by Django 3.2.9 on 2021-11-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appperformance',
            name='date',
            field=models.DateField(),
        ),
    ]
