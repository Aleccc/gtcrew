# Generated by Django 4.1 on 2023-02-21 03:34

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0023_title_expire_at_title_expired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='profiles',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, through='team.Membership', to='team.profile'),
        ),
    ]