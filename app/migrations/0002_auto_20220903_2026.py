# Generated by Django 2.0.4 on 2022-09-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]