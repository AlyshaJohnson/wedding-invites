# Generated by Django 3.2.16 on 2022-11-10 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invite', '0009_auto_20221107_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='guest_id',
        ),
        migrations.AlterField(
            model_name='guest',
            name='user_id',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue1_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='venue2_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='wedding_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
