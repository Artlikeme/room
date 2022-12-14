# Generated by Django 4.1 on 2022-08-07 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='namePerson')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('active', models.BooleanField(verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='Start date')),
                ('end', models.DateField(verbose_name='End date')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rooms')),
            ],
        ),
    ]
