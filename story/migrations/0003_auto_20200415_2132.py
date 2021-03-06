# Generated by Django 3.0.4 on 2020-04-16 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20200415_2132'),
        ('story', '0002_auto_20200411_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-date_updated'], 'verbose_name': 'story', 'verbose_name_plural': 'stories'},
        ),
        migrations.AlterField(
            model_name='story',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stories_created', to='team.Profile'),
        ),
        migrations.AlterField(
            model_name='story',
            name='profiles_mentioned',
            field=models.ManyToManyField(blank=True, related_name='stories_mentioned', to='team.Profile'),
        ),
    ]
