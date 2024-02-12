# Generated by Django 4.1.7 on 2023-03-15 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_blogcategory_blogsubcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('short_dsc', models.CharField(max_length=250)),
                ('dsc', models.TextField()),
                ('slug', models.CharField(default='title-with', max_length=550)),
                ('post_keywords', models.CharField(max_length=550)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('image_caption', models.CharField(default='default-image-caption', max_length=200)),
                ('review_status', models.CharField(choices=[('1', 'Pending'), ('2', 'Published'), ('3', 'Rejected')], default='2', max_length=1)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.blogcategory')),
                ('subcategory', models.ForeignKey(blank=True, default='', max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.blogsubcategory')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
