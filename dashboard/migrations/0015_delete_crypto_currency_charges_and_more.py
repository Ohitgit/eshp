# Generated by Django 4.1.7 on 2023-07-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_dp_add_fund_request'),
    ]

    operations = [
        migrations.DeleteModel(
            name='crypto_currency_charges',
        ),
        migrations.DeleteModel(
            name='dp_add_fund_request',
        ),
        migrations.AddField(
            model_name='blog',
            name='dsc1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='dsc2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='siteengineer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='write',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='dp_members',
        ),
    ]
