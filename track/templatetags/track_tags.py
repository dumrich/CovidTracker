from django import template

register = template.Library()


@register.filter(name="is_str")
def is_str(value):
    return type(value).__name__
