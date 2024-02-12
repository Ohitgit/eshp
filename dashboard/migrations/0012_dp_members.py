# Generated by Django 4.1.7 on 2023-05-10 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0011_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='dp_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('pwd1', models.CharField(max_length=100)),
                ('pwd2', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('account_type', models.CharField(choices=[('P', 'Personal Account'), ('M', 'Merchant Account'), ('LD', 'Local Depositor')], max_length=255)),
                ('status', models.CharField(choices=[('V', 'Verified'), ('U', 'Unverified')], default='U', max_length=1)),
                ('is_active', models.IntegerField(choices=[(0, False), (1, True)], default=1)),
                ('is_deleted', models.IntegerField(choices=[(0, False), (1, True)], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
