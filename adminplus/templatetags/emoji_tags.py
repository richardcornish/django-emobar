from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.utils.safestring import mark_safe

from adminplus.templatetags.emoji_dict import emoji_dict

import re


register = template.Library()


emoji_finder = re.compile(u':[\w]+:')


@register.filter
@stringfilter
def emoji(value):
    for emoji in set(emoji_finder.findall(value)):
        if emoji in emoji_dict:
            value = value.replace(emoji, u'<span class="emoji"><img src="' + settings.STATIC_URL + 'adminplus/img/%s" height="22" width="22" alt="%s"></span>' % (emoji_dict[emoji], emoji[1:-1]))
    return mark_safe(value)
