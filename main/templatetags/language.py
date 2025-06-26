from django import template
from django.utils.translation import get_language

register = template.Library()

@register.filter
def i18n(obj, field_base):
    lang = get_language()
    field_name = f"{field_base}_{lang}"
    return getattr(obj, field_name, '') or getattr(obj, f"{field_base}_en", '')