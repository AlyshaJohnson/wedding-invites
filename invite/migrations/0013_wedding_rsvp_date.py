# Generated by Django 3.2.16 on 2022-11-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0012_auto_20221121_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='rsvp_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
