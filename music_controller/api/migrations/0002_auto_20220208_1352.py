# Generated by Django 3.1.7 on 2022-02-08 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='quest_can_pause',
            new_name='guest_can_pause',
        ),
    ]
