# Generated by Django 4.0.6 on 2022-10-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0004_rename_user_name_registration_user_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='abroad',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
