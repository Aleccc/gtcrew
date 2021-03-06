from django.db import models
from django.forms import widgets
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcaptcha.models import WagtailCaptchaEmailForm

from gtcrew.blocks import PostBlock, BaseStreamBlock


class GenericPage(Page):
    body = StreamField([
        ('post', PostBlock()),
        ('section', BaseStreamBlock()),
        ('html', blocks.RawHTMLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(WagtailCaptchaEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('post', PostBlock()),
        ('section', BaseStreamBlock())
    ])
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields", classname="form-control"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    subpage_types = []

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for name, field in form.fields.items():
            if isinstance(field.widget, widgets.ChoiceWidget):
                css_classes = field.widget.attrs.get('class', '').split()
                css_classes.append('custom-select')
                field.widget.attrs.update({'class': ' '.join(css_classes)})
            else:
                css_classes = field.widget.attrs.get('class', '').split()
                css_classes.append('form-control')
                field.widget.attrs.update({'class': ' '.join(css_classes)})
            field.widget.attrs['aria-describedby'] = 'id_%s' % name  # slug version
            field.widget.attrs['aria-label'] = '%s' % field.label  # title version
            field.widget.attrs['placeholder'] = '%s' % field.label
        return form


@register_setting(icon='fa-picture-o')
class Favicon(BaseSetting):
    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('favicon'),
    ]
