# Generated by Django 4.1.7 on 2023-07-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_blog_siteengineerimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(null=True)),
                ('name', models.CharField(max_length=80, null=True)),
                ('email', models.CharField(max_length=80, null=True)),
                ('img', models.ImageField(null=True, upload_to='image')),
            ],
        ),
    ]