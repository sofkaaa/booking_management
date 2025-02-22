# Generated by Django 5.1.6 on 2025-02-22 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('specs', models.TextField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PCRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('numder', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('available', models.BooleanField(default=True)),
                ('computers', models.ManyToManyField(to='booking.computer')),
            ],
        ),
        migrations.CreateModel(
            name='BookedPCRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('pcroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.pcroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.uprofile')),
            ],
        ),
        migrations.CreateModel(
            name='BookedComputer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.computer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.uprofile')),
            ],
        ),
    ]
