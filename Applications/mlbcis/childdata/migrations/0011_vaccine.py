# Generated by Django 4.0.4 on 2023-04-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childdata', '0010_alter_doctor_epass_alter_doctor_fname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.TextField()),
                ('days', models.TextField()),
                ('vaccine', models.TextField()),
                ('due', models.TextField()),
                ('max', models.TextField()),
                ('Dose', models.TextField()),
                ('route', models.TextField()),
                ('disease', models.TextField()),
                ('symptoms', models.TextField()),
                ('precautions', models.TextField()),
            ],
        ),
    ]