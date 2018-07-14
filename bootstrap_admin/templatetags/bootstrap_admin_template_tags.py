import django
from django.contrib.admin import site
from django.apps import apps
from django.utils.text import capfirst
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.module_loading import import_string
from django.conf import settings
from django import template
from django import VERSION as DJANGO_VERSION

# Depending on you python version, reduce has been moved to functools
try:
    from functools import reduce
except ImportError:
    pass


# Depending on your django version, `reverse` and `NoReverseMatch` has been moved.
# From django 2.0 they've been moved to `django.urls`
try:
    from django.urls import reverse, NoReverseMatch
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

# From django 1.9 `assignment_tag` is deprecated in favour of `simple_tag`
try:
    simple_tag = register.simple_tag
except AttributeError:
    simple_tag = register.assignment_tag


MAX_LENGTH_BOOTSTRAP_COLUMN = 12


def css_classes_for_field(field, custom_classes):
    orig_class = field.field.widget.attrs.get('class', '')
    required = 'required' if field.field.required else ''
    classes = field.css_classes(' '.join([orig_class, custom_classes, required]))
    return classes


@register.filter()
def get_label(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    return field.label_tag(attrs={'class': classes}, label_suffix='')


@register.filter()
def add_class(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    try:
        # For widgets like SelectMultiple, checkboxselectmultiple
        field.field.widget.widget.attrs.update({'class': classes})
    except:
        field.field.widget.attrs.update({'class': classes})
    return field


@register.filter()
def widget_type(field):
    if isinstance(field, dict):
        return 'adminreadonlyfield'
    try:
        # For widgets like SelectMultiple, checkboxselectmultiple
        widget_type = field.field.widget.widget.__class__.__name__.lower()
    except:
        widget_type = field.field.widget.__class__.__name__.lower()
    return widget_type


@register.filter()
def placeholder(field, placeholder=''):
    field.field.widget.attrs.update({'placeholder': placeholder})
    return field


def sidebar_menu_setting():
    return getattr(settings, 'BOOTSTRAP_ADMIN_SIDEBAR_MENU', True)


@simple_tag
def display_sidebar_menu(has_filters=False):
    if has_filters:
        # Always display the menu in change_list.html
        return True
    return sidebar_menu_setting()


@register.filter()
def has_active_menu(app, current_url):
    return current_url in [item['admin_url'] for item in app['models']]


def sidebar_menu_list(sidebar_menu_callback, request):
    """
    Adapted from https://github.com/maykinmedia/django-admin-index
    """

    show_remaining_apps = getattr(settings, 'BOOTSTRAP_ADMIN_SHOW_REMAINING_APPS', False) or \
        (getattr(settings, 'BOOTSTRAP_ADMIN_SHOW_REMAINING_APPS_TO_SUPERUSERS', True) and request.user.is_superuser)

    sidebar_menu_callback_func = import_string(sidebar_menu_callback)
    sidebar_menu_items = sidebar_menu_callback_func(request)

    # Convert to convienent dict
    model_dicts = {}

    if django.VERSION < (1, 9):
        from .compat.django18 import get_app_list
        original_app_list = get_app_list(site, request)
    else:
        original_app_list = site.get_app_list(request)

    for app in original_app_list:
        for model in app['models']:
            key = '{}.{}'.format(app['app_label'], model['object_name'].lower())  # noqa
            model_dict = model.copy()
            model_dict.update({
                'app_label': app['app_label'],
                'app_name': app['name'],
                'app_url': app['app_url'],
                'has_module_perms': app['has_module_perms'],
            })
            model_dicts[key] = model_dict

    # Create new list based on our groups, using the model_dicts constructed above.
    added = []
    result = []
    app_list = sidebar_menu_items

    for app in app_list:
        models = []
        for item in app['items']:
            if 'model' in item:
                key = item['model']
                o = model_dicts.get(key)
                if o:
                    models.append(o)
                    added.append(key)
            elif 'link' in item:
                models.append({
                    'name': item['name'],
                    'app_label': app['app_label'],
                    'admin_url': item['link'],
                    'object_name': item['object_name'],
                })

        result.append({
            'name': app['name'],
            'app_label': app['app_label'],
            'models': models,
        })

    if show_remaining_apps:
        other = [model_dicts[k] for k in model_dicts if k not in added]
        if other:
            result.append({
                'name': ('Miscellaneous'),
                'app_label': 'misc',
                'models': sorted(other, key=lambda m: m['name'])
            })

    return result


@register.inclusion_tag('bootstrap_admin/sidebar_menu.html',
                        takes_context=True)
def render_menu_app_list(context):
    show_global_menu = sidebar_menu_setting()
    if not show_global_menu:
        return {'app_list': ''}

    sidebar_menu_callback = getattr(settings, 'BOOTSTRAP_ADMIN_SIDEBAR_MENU_CALLBACK', None)
    if sidebar_menu_callback:
        return {
            'app_list': sidebar_menu_list(sidebar_menu_callback, context.get('request')),
            'current_url': context.get('request').path,
        }

    if DJANGO_VERSION < (1, 8):
        dependencie = 'django.core.context_processors.request'
        processors = settings.TEMPLATE_CONTEXT_PROCESSORS
        dependency_str = 'settings.TEMPLATE_CONTEXT_PROCESSORS'
    else:
        dependencie = 'django.template.context_processors.request'
        implemented_engines = getattr(settings, 'BOOTSTRAP_ADMIN_ENGINES',
            ['django.template.backends.django.DjangoTemplates'])
        dependency_str = "the 'context_processors' 'OPTION' of one of the " + \
            "following engines: %s" % implemented_engines
        filtered_engines = [engine for engine in settings.TEMPLATES
            if engine['BACKEND'] in implemented_engines]
        if len(filtered_engines) == 0:
            raise ImproperlyConfigured(
                "bootstrap_admin: No compatible template engine found" +
                "bootstrap_admin requires one of the following engines: %s"
                % implemented_engines
            )
        processors = reduce(lambda x, y: x.extend(y), [
            engine.get('OPTIONS', {}).get('context_processors', [])
            for engine in filtered_engines])

    if dependencie not in processors:
        raise ImproperlyConfigured(
            "bootstrap_admin: in order to use the 'sidebar menu' requires" +
            " the '%s' to be added to %s"
            % (dependencie, dependency_str)
        )

    # Code adapted from django.contrib.admin.AdminSite
    app_dict = {}
    user = context.get('user')
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(context.get('request'))

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                }
                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse(
                            'admin:%s_%s_changelist' % info,
                            current_app=site.name
                        )
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse(
                            'admin:%s_%s_add' % info,
                            current_app=site.name
                        )
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'name': apps.get_app_config(app_label).verbose_name,
                        'app_label': app_label,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=site.name
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # Sort the apps alphabetically.
    app_list = list(six.itervalues(app_dict))
    app_list.sort(key=lambda x: x['name'].lower())

    # Sort the models alphabetically within each sapp.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])

    return {'app_list': app_list, 'current_url': context.get('request').path}


@register.filter()
def class_for_field_boxes(line):
    size_column = MAX_LENGTH_BOOTSTRAP_COLUMN // len(line.fields)
    return 'col-sm-{0}'.format(size_column or 1)  # if '0' replace with 1
