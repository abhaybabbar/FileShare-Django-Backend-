# Generated by Django 4.0.2 on 2022-02-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
