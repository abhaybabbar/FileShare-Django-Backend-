# Generated by Django 3.1.7 on 2022-02-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220202_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileshare',
            name='files',
            field=models.ManyToManyField(to='main.File'),
        ),
    ]