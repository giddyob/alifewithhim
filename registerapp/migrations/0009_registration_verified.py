# Generated by Django 4.0.6 on 2022-11-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0008_remove_registration_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]