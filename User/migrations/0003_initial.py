# Generated by Django 5.0.2 on 2024-04-01 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0016_tbl_newhotel'),
        ('Hotel', '0013_delete_tbl_floor'),
        ('User', '0002_delete_tbl_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_checkin', models.DateField()),
                ('booking_checkout', models.DateField()),
                ('booking_noofguest', models.CharField(max_length=50)),
                ('booking_amount', models.IntegerField(default='0')),
                ('booking_status', models.IntegerField(default='0')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhotel')),
                ('mealpackages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_mealpackages')),
                ('pickanddrophead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_pickanddrophead')),
                ('tourpackages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.tbl_tourpackages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
