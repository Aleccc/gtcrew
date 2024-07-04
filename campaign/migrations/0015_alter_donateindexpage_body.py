# Generated by Django 4.1.13 on 2024-07-04 16:29

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0014_alter_donateindexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateindexpage',
            name='body',
            field=wagtail.fields.StreamField([('post', wagtail.blocks.StructBlock([('heading_small', wagtail.blocks.CharBlock()), ('heading_large', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('section', wagtail.blocks.StreamBlock([('heading_group_block', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('display-1', 'Display 1'), ('display-2', 'Display 2'), ('display-3', 'Display 3'), ('display-4', 'Display 4'), ('display-5', 'Display 5'), ('display-6', 'Display 6')], required=False)), ('font_color', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Default'), ('text-muted', 'Muted'), ('text-primary', 'Primary'), ('text-secondary', 'Secondary'), ('text-light', 'Light'), ('text-dark', 'Dark')], required=False)), ('font_alignment', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')], required=False))]))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='link', template='blocks/embed_block.html'))]))], use_json_field=True),
        ),
    ]