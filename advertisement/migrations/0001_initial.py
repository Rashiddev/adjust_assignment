# Generated by Django 3.2.9 on 2021-11-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('channel', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('os', models.CharField(choices=[('android', 'android'), ('ios', 'ios')], default='android', max_length=7)),
                ('impression', models.PositiveBigIntegerField()),
                ('clicks', models.PositiveIntegerField()),
                ('installs', models.PositiveIntegerField()),
                ('spend', models.PositiveBigIntegerField()),
                ('revenue', models.PositiveBigIntegerField()),
            ],
        ),
    ]
