# Generated by Django 3.0.4 on 2020-06-07 11:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.fields.StreamField([('post', wagtail.blocks.StructBlock([('heading_small', wagtail.blocks.CharBlock()), ('heading_large', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
