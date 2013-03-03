from django.contrib.admin.templatetags.admin_list import *


@register.simple_tag
def paginator_number(cl, i):
    """
    Generates an individual page index link in a paginated list.
    """
    if i == DOT:
        return u'<li class="disabled"><a href="#">...</a></li>'
    elif i == cl.page_num:
        return format_html(u'<li class="active"><a href="#">{0}</a></li> ', i+1)
    else:
        return format_html(u'<li><a href="{0}"{1}>{2}</a></li>', cl.get_query_string({PAGE_VAR: i}), mark_safe(' class="end"' if i == cl.paginator.num_pages-1 else ''), i+1)
