# Generated by Django 4.0.4 on 2022-06-01 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_organiser',
            new_name='is_organisor',
        ),
    ]