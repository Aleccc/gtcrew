# Generated by Django 3.0.7 on 2020-07-14 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='held_by',
            field=models.CharField(choices=[('student', 'Student'), ('coach', 'Coach'), ('alumni', 'Alumni'), ('racer', 'Racer')], default='student', max_length=7),
        ),
    ]
