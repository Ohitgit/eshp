# Generated by Django 4.1.7 on 2023-07-25 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_delete_slider_about_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=80, null=True)),
                ('website', models.CharField(max_length=80, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='dashboard.comment')),
            ],
        ),
    ]
