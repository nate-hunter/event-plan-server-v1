# Generated by Django 4.2.5 on 2023-11-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_cost_alter_event_cost_per_guest_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_pinned',
        ),
    ]
