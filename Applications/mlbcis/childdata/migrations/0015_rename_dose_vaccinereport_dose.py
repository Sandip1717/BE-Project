# Generated by Django 4.0.4 on 2023-05-01 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('childdata', '0014_vaccinereport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccinereport',
            old_name='Dose',
            new_name='dose',
        ),
    ]
