# Generated by Django 3.2.12 on 2022-03-06 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shellpage',
            name='name',
        ),
    ]
