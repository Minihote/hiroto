# Generated by Django 5.0.2 on 2024-04-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0004_rename_room_type_tbl_roomtype_roomtype_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.CharField(max_length=50)),
            ],
        ),
    ]
