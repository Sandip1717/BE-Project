# Generated by Django 4.0.4 on 2023-05-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childdata', '0012_delete_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=125)),
                ('photo', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=125)),
                ('mobile', models.CharField(max_length=125)),
                ('cname', models.CharField(max_length=125)),
                ('cdob', models.CharField(max_length=125)),
                ('uname', models.CharField(max_length=125)),
                ('hid', models.CharField(max_length=125)),
                ('hname', models.CharField(max_length=125)),
                ('epass', models.CharField(max_length=125)),
            ],
        ),
    ]