# Generated by Django 4.2.3 on 2023-07-27 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service', models.CharField(choices=[('O', 'Oil & Filter'), ('T', 'Rotate Tires'), ('B', 'Brake(s) Replacement')], default='O', max_length=1)),
                ('description', models.TextField(max_length=250)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
