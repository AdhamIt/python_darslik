# Generated by Django 4.0.4 on 2022-04-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('tami', models.CharField(max_length=200)),
                ('rangi', models.CharField(max_length=200)),
            ],
        ),
    ]
