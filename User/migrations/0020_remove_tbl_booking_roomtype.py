# Generated by Django 5.0.4 on 2024-04-26 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_tbl_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='roomtype',
        ),
    ]