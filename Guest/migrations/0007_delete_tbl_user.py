# Generated by Django 5.0.2 on 2024-03-16 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]