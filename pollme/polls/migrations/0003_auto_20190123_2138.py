# Generated by Django 2.0.2 on 2019-01-23 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='poll',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
