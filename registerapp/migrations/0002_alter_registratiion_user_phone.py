# Generated by Django 4.0.6 on 2022-10-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registratiion',
            name='user_phone',
            field=models.CharField(max_length=15),
        ),
    ]
