# Generated by Django 4.1.7 on 2023-07-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_alter_about_content_alter_about_content1'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='content3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='img1',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='about',
            name='img2',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]