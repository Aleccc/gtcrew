# Generated by Django 3.0.8 on 2020-08-15 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0017_auto_20200713_2157'),
        ('wagtailcore', '0052_pagelogentry'),
        ('event', '0016_auto_20200814_2141'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RacerInline',
            new_name='Racer',
        ),
        migrations.RenameModel(
            old_name='ResultInline',
            new_name='Result',
        ),
    ]