# Generated by Django 4.1.3 on 2023-02-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_notes_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='subcategory',
        ),
    ]
