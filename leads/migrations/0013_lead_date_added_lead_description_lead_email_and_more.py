# Generated by Django 4.0.5 on 2022-06-22 17:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_alter_lead_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
