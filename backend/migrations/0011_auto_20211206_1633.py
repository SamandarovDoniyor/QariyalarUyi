# Generated by Django 3.1 on 2021-12-06 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20211206_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archive',
            old_name='image_elderly_archive',
            new_name='image_archive',
        ),
    ]
