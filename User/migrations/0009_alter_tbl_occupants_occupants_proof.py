# Generated by Django 5.0.2 on 2024-04-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_rename_occupantsr_proof_tbl_occupants_occupants_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_occupants',
            name='occupants_proof',
            field=models.FileField(upload_to='Assets/OccupantsProof/'),
        ),
    ]