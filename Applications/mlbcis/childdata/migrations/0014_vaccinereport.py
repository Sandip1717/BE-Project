# Generated by Django 4.0.4 on 2023-05-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childdata', '0013_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccinereport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.TextField()),
                ('age', models.TextField()),
                ('vaccine', models.TextField()),
                ('due', models.TextField()),
                ('max', models.TextField()),
                ('given', models.TextField()),
                ('Dose', models.TextField()),
                ('route', models.TextField()),
                ('disease', models.TextField()),
                ('symptoms', models.TextField()),
                ('precautions', models.TextField()),
                ('cid', models.TextField()),
                ('cname', models.TextField()),
                ('cphoto', models.TextField()),
                ('pname', models.TextField()),
                ('did', models.TextField()),
                ('dname', models.TextField()),
                ('hname', models.TextField()),
                ('height', models.TextField()),
                ('weight', models.TextField()),
                ('action', models.TextField()),
            ],
        ),
    ]