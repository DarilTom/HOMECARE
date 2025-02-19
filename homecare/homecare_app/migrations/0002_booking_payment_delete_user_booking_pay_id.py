# Generated by Django 5.1.6 on 2025-02-19 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecare_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_time', models.DateTimeField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homecare_app.service')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homecare_app.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('working_hour', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='booking',
            name='pay_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homecare_app.payment'),
        ),
    ]
