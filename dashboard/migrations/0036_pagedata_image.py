# Generated by Django 4.1.7 on 2023-08-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_pagedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagedata',
            name='image',
            field=models.ImageField(blank=True, upload_to='qrcode'),
        ),
    ]
