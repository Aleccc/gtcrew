# Generated by Django 3.0.4 on 2020-06-11 02:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gtid', models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator('^(\\d){9}$')], verbose_name='GT ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('major', models.CharField(blank=True, max_length=64)),
                ('hometown', models.CharField(blank=True, max_length=64)),
                ('bio', wagtail.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
            bases=('wagtailcore.page',),
        ),
    ]
