# Generated by Django 5.0.2 on 2024-04-02 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_alter_tbl_occupants_occupants_proof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_occupants',
            name='booking',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
    ]
