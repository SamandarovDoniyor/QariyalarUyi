# Generated by Django 3.1 on 2021-12-03 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_donat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donat',
            options={'verbose_name': 'Hayriya', 'verbose_name_plural': 'Hayriyalar'},
        ),
        migrations.RenameField(
            model_name='donat',
            old_name='description',
            new_name='body',
        ),
    ]
