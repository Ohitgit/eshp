# Generated by Django 4.1.7 on 2023-07-23 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_slide1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slider',
        ),
    ]
