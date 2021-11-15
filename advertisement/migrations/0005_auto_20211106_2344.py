# Generated by Django 3.2.9 on 2021-11-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_rename_impression_appperformance_impressions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appperformance',
            name='revenue',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='appperformance',
            name='spend',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]