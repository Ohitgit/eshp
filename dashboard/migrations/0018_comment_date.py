# Generated by Django 4.1.7 on 2023-07-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
