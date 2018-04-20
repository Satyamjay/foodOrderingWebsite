# Generated by Django 2.0.4 on 2018-04-19 15:42

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableState',
            fields=[
                ('state_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AvailableState')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_no', models.CharField(max_length=10, unique=True, validators=[app.models.validate_mobile])),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('manager_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_no', models.CharField(max_length=10, unique=True, validators=[app.models.validate_mobile])),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=8, validators=[app.models.validate_pincode])),
                ('street_address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
                ('unique_id', models.CharField(max_length=256)),
            ],
        ),
    ]
