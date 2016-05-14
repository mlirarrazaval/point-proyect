from django.template import Library
from django.core.urlresolvers import reverse

register = Library()


@register.simple_tag
def active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return 'active'
    return ''
