from django.contrib.admin.templatetags.admin_list import *


@register.simple_tag
def paginator_number(cl, i):
    """
    Generates an individual page index link in a paginated list.
    """
    if i == DOT:
        return u'<li class="disabled"><a href="#">...</a></li>'
    elif i == cl.page_num:
        return mark_safe(u'<li class="active"><a href="#">%d</a></li> ' % (i + 1))
    else:
        return mark_safe(u'<li><a href="%s">%d</a></li>' % (escape(cl.get_query_string({PAGE_VAR: i})), i + 1))
