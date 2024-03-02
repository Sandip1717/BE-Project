# Generated by Django 4.0.4 on 2023-04-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childdata', '0006_remove_imagef_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('photo', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=25)),
                ('cname', models.CharField(max_length=25)),
                ('cdob', models.CharField(max_length=25)),
                ('uname', models.CharField(max_length=25)),
                ('hname', models.CharField(max_length=25)),
                ('epass', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]