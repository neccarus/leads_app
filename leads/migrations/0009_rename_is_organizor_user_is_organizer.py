# Generated by Django 4.0.4 on 2022-06-14 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_rename_organisation_agent_organization_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_organizor',
            new_name='is_organizer',
        ),
    ]
