# Generated by Django 4.0.6 on 2022-10-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0005_registration_abroad'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='coming_with_kids',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='registration',
            name='num_of_kids',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
