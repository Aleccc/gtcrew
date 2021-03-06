# Generated by Django 2.0.7 on 2020-03-27 04:34

from django.db import migrations, models
import team.validators


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, upload_to='', validators=[team.validators.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='post',
            name='document_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
