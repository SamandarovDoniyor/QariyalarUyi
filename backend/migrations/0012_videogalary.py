# Generated by Django 3.1 on 2021-12-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20211206_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(max_length=255)),
                ('video_title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videolar',
            },
        ),
    ]
