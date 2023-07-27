# Generated by Django 4.2.3 on 2023-07-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=75)),
                ('year', models.IntegerField()),
                ('engine', models.CharField(max_length=20)),
            ],
        ),
    ]
