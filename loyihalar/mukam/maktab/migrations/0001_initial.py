# Generated by Django 4.0.4 on 2022-04-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maktab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('manzili', models.CharField(max_length=200)),
                ('uquvchi_soni', models.IntegerField()),
                ('about', models.TextField()),
            ],
        ),
    ]
