import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('working_hour', models.IntegerField()),
            ],
        ),
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, max_length=5, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('housename', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('worker_district', models.CharField(default='Unknown', max_length=100)),
                ('worker_town', models.CharField(default='Unknown', max_length=100)),
                ('worker_housename', models.CharField(default='Unknown', max_length=255)),
                ('worker_photo', models.ImageField(blank=True, null=True, upload_to='worker_photos/')),
                ('servicecatagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='homecare_app.service')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('pay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_bookings', to='homecare_app.payment')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_bookings', to='homecare_app.service')),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_bookings', to='homecare_app.worker')),
            ],
        ),
    ]
