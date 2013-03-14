"""
These functions bellow are from django-widget-tweaks.
(silence_without_field, _process_field_attributes, append_attr, add_class, widget_type)

By Mikhail Korobov and contributors, more information:
Copyright (c) 2011 Mikhail Korobov
LICENSE: https://github.com/kmike/django-widget-tweaks/blob/master/LICENSE
"""

from django.contrib.admin.models import LogEntry
from django import template
register = template.Library()


def silence_without_field(fn):
    def wrapped(field, attr):
        if not field:
            return ""
        else:
            return fn(field, attr)
    return wrapped


def _process_field_attributes(field, attr, process):

    # split attribute name and value from 'attr:value' string
    params = attr.split(':', 1)
    attribute = params[0]
    value = params[1] if len(params) == 2 else ''

    # decorate field.as_widget method with updated attributes
    old_as_widget = field.as_widget

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        attrs = attrs or {}
        process(widget or self.field.widget, attrs, attribute, value)
        return old_as_widget(widget, attrs, only_initial)

    bound_method = type(old_as_widget)
    try:
        field.as_widget = bound_method(as_widget, field, field.__class__)
    except TypeError: # python 3
        field.as_widget = bound_method(as_widget, field)
    return field


@register.filter("append_attr")
@silence_without_field
def append_attr(field, attr):
    def process(widget, attrs, attribute, value):
        if attrs.get(attribute):
            attrs[attribute] += ' ' + value
        elif widget.attrs.get(attribute):
            attrs[attribute] = widget.attrs[attribute] + ' ' + value
        else:
            attrs[attribute] = value
    return _process_field_attributes(field, attr, process)


@register.filter("add_class")
@silence_without_field
def add_class(field, css_class):
    return append_attr(field, 'class:' + css_class)


@register.filter(name='widget_type')
def widget_type(field):
    """
    Template filter that returns field widget class name (in lower case).
    E.g. if field's widget is TextInput then {{ field|widget_type }} will
    return 'textinput'.
    """
    if hasattr(field, 'field') and hasattr(field.field, 'widget') and field.field.widget:
        return field.field.widget.__class__.__name__.lower()
    return ''


class AdminLogNode(template.Node):
    """
        NOTE: I've changed the original behaviour in order to provide a
        Admin Log for a specific app on the AdminSite.app_index.
    """
    def __init__(self, limit, varname, user):
        self.limit, self.varname, self.user = limit, varname, user

    def __repr__(self):
        return "<GetAdminLog Node>"

    def render(self, context):
        app_label = context.get('app_label')
        if app_label:
            if self.user is None:
                context[self.varname] = LogEntry.objects.filter(content_type__app_label__exact=app_label).select_related('content_type', 'user')[:self.limit]
            else:
                user_id = self.user
                if not user_id.isdigit():
                    user_id = context[self.user].id
                context[self.varname] = LogEntry.objects.filter(user__id__exact=user_id, content_type__app_label__exact=app_label).select_related('content_type', 'user')[:int(self.limit)]
        return ''


@register.tag
def get_admin_log_for_app(parser, token):
    """
    NOTE: I've changed the original behaviour in order to provide a
    Admin Log for a specific app on the AdminSite.app_index.

    Populates a template variable with the admin log for the given criteria.

    Usage::

        {% get_admin_log_for_app [limit] as [varname] for_user [context_var_containing_user_obj] %}

    Examples::

        {% get_admin_log_for_app 10 as admin_log for_user 23 %}
        {% get_admin_log_for_app 10 as admin_log for_user user %}
        {% get_admin_log_for_app 10 as admin_log %}

    Note that ``context_var_containing_user_obj`` can be a hard-coded integer
    (user ID) or the name of a template context variable containing the user
    object whose ID you want.
    """
    tokens = token.contents.split()
    if len(tokens) < 4:
        raise template.TemplateSyntaxError(
            "'get_admin_log_for_app' statements require two arguments")
    if not tokens[1].isdigit():
        raise template.TemplateSyntaxError(
            "First argument to 'get_admin_log_for_app' must be an integer")
    if tokens[2] != 'as':
        raise template.TemplateSyntaxError(
            "Second argument to 'get_admin_log_for_app' must be 'as'")
    if len(tokens) > 4:
        if tokens[4] != 'for_user':
            raise template.TemplateSyntaxError(
                "Fourth argument to 'get_admin_log_for_app' must be 'for_user'")
    return AdminLogNode(limit=tokens[1], varname=tokens[3], user=(len(tokens) > 5 and tokens[5] or None))


@register.filter
def user_admin_urlname(value, arg):
    '''
    Providing a link to change the user
    (for working better with auth custom user)
    '''
    return 'admin:%s_%s_%s' % (value._meta.app_label, value._meta.module_name, arg)
