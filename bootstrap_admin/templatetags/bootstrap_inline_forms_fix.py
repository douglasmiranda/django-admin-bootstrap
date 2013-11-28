"""
In Django < 1.6 when you define custom pk in yur model and make it not not
editable and put it to inline_form you will get an error because this pk is
not added to form due to known bug https://code.djangoproject.com/ticket/13696

Filter below makes backward compatible fix for this problem
"""

from django import template
register = template.Library()

@register.filter
def needs_explicit_pk_field(inline_form):
    try:
        # Expecting django >= 1.6
        result = inline_form.needs_explicit_pk_field()
    except AttributeError:
        # Dealing with django < 1.6
        result = inline_form.has_auto_field()

        # Additional check added in django 1.6
        if not result and not inline_form.form._meta.model._meta.pk.editable:
            result = True

    return result
