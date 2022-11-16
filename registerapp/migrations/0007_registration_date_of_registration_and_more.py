# Generated by Django 4.0.6 on 2022-11-11 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0006_registration_coming_with_kids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='date_of_registration',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='registration',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]