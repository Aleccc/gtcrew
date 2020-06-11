from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldRowPanel, FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class PersonPage(Page):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    gtid = models.CharField("GT ID", max_length=9, blank=True,
                            validators=[RegexValidator(r'^(\d){9}$')])
    birthday = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=64, blank=True)
    hometown = models.CharField(max_length=64, blank=True)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name_plural = 'People'

    # def clean(self):
    #     """Override the values of title and slug before saving."""
    #     # super(MatchPage, self).clean() # Python 2.X syntax
    #     super().clean()
    #     self.title = '%s %s' % (self.first_name, self.last_name)
    #     self.slug = slugify(self.title)

    content_panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        ImageChooserPanel('image'),
        FieldPanel('bio', classname="collapsible"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('birthday', classname="col6"),
                FieldPanel('hometown', classname="col6"),
                FieldPanel('gtid', classname="col6"),
                FieldPanel('major', classname="col6"),
            ])
        ], "Details"),
    ]

    parent_page_types = ['PersonIndexPage']
    subpage_types = []


# # set a default blank slug for when the editing form renders
# # we set this after the model is declared
# PersonPage._meta.get_field('slug').default = 'default-blank-slug'


class PersonIndexPage(Page):
    subpage_types = ['PersonPage']

    def get_people(self):
        return PersonPage.objects.live().descendant_of(
            self).order_by('last_name')

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_people(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request, *args, **kwargs):
        context = super(PersonIndexPage, self).get_context(request)

        # PersonPage objects (get_people) are passed through pagination
        people = self.paginate(request, self.get_people())

        context['people'] = people

        return context
