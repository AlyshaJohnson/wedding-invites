# Generated by Django 3.2.16 on 2022-11-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0006_alter_guest_linked_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='linked_party',
            field=models.ManyToManyField(blank=True, related_name='_invite_guest_linked_party_+', to='invite.Guest'),
        ),
    ]