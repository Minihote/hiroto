# Generated by Django 5.0.2 on 2024-04-02 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0015_tbl_specialized'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_specialized',
            old_name='speci',
            new_name='specialized_name',
        ),
    ]
