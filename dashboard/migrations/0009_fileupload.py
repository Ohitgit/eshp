# Generated by Django 4.1.7 on 2023-04-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('desc', models.TextField()),
                ('upload', models.FileField(upload_to='doc')),
            ],
        ),
    ]
