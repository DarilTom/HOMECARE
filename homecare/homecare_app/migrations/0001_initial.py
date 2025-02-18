# Generated by Django 5.1.6 on 2025-02-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_desc', models.TextField()),
                ('service_rate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_pass', models.CharField(max_length=100)),
                ('user_blood', models.CharField(max_length=3)),
                ('user_phone', models.CharField(max_length=15)),
                ('user_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.AutoField(primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=100)),
                ('worker_email', models.EmailField(max_length=100)),
                ('worker_pass', models.CharField(max_length=100)),
                ('worker_phone', models.CharField(max_length=15)),
                ('worker_dob', models.DateField()),
                ('worker_blood', models.CharField(max_length=3)),
                ('worker_address', models.TextField()),
            ],
        ),
    ]
