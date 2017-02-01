import re

from django.core.urlresolvers import reverse, NoReverseMatch

from django.template import Library

register = Library()


@register.simple_tag(takes_context=True)
def url_match(context, pattern_or_urlname, output):
    """
    Given a certain URL to match against, returns the output string if a match
    is found, or a blank string if not.
    """
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return output
    return ''
