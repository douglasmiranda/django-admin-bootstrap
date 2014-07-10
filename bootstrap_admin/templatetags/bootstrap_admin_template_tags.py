from django import template
register = template.Library()


def css_classes_for_field(field, custom_classes):
    required = 'required' if field.field.required else ''
    classes = field.css_classes('{} {}'.format(custom_classes, required))
    return classes


@register.filter()
def get_label(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    return field.label_tag(attrs={'class': classes}, label_suffix='')


@register.filter()
def add_class(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    field.field.widget.attrs.update({'class': classes})
    return field


@register.filter()
def placeholder(field, placeholder=''):
    field.field.widget.attrs.update({'placeholder': placeholder})
    return field
