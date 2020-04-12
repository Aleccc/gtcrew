# Generated by Django 3.0.4 on 2020-04-12 02:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20200407_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['last_name'], 'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('unclaimed', 'Unclaimed'), ('pending', 'Pending Approval'), ('approved', 'Approved')], default='unclaimed', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gtid',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator('^(\\d){9}$')], verbose_name='GT ID'),
        ),
    ]
