# Generated by Django 3.2.16 on 2022-11-07 14:54

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0003_auto_20221107_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='allergies',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='diet',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='guest',
            name='RSVP',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='RSVP_comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='guest',
            name='hotel',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='guest',
            name='party_admin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='dessert1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='dessert2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='dessert3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='main1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='main2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='main3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='menu',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='other_info',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='starter1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='starter1_ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='starter2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='starter3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue1_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue1_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue2_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue2_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='wedding_date',
            field=models.DateField(blank=True),
        ),
    ]
