# Generated by Django 3.1 on 2021-12-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_image', models.ImageField(default='imges/default.jpg', upload_to='images/')),
                ('partner_title', models.CharField(max_length=255)),
                ('partner_body', models.TextField(max_length=255)),
                ('partner_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Fikr', 'verbose_name_plural': 'Fikrlar'},
        ),
    ]
