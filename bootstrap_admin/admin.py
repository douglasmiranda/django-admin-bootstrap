from django.contrib import admin
from django.core.urlresolvers import reverse
from functools import wraps


def context_data_for_app_index(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.context_data['app_label'] = kwargs.get('app_label')
        response.context_data['is_app_index'] = True
        response.context_data['admin_root_url'] = reverse('admin:index')
        return response
    return _wrapper

admin.site.__class__.app_index = context_data_for_app_index(admin.site.__class__.app_index)
