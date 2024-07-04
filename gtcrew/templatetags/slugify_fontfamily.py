from django import template

register = template.Library()


@register.filter
def slugify_fontfamily(value):
    return value.replace(' ', '+')
