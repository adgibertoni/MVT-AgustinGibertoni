# Generated by Django 4.1.2 on 2022-10-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
                ('fav_number', models.IntegerField()),
            ],
        ),
    ]