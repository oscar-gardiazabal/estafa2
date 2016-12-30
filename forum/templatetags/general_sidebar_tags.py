from django import template
from forum.models import Tag, Award, MarkedTag
from forum import settings

from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from forum.templatetags import argument_parser

from extra_filters import static_content

register = template.Library()

@register.inclusion_tag('sidebar/markdown_help.html')
def markdown_help():
    return {}

@register.inclusion_tag('sidebar/recent_awards.html')
def recent_awards():
    return {'awards': Award.objects.order_by('-awarded_at')[:settings.RECENT_AWARD_SIZE]}

@register.inclusion_tag('sidebar/user_blocks.html')
def sidebar_upper():
    return {
        'show': settings.SIDEBAR_UPPER_SHOW,
        'content': static_content(settings.SIDEBAR_UPPER_TEXT, settings.SIDEBAR_UPPER_RENDER_MODE),
        'wrap': not settings.SIDEBAR_UPPER_DONT_WRAP,
        'blockid': 'sidebar-upper'
    }

@register.inclusion_tag('sidebar/user_blocks.html')
def sidebar_lower():
    return {
        'show': settings.SIDEBAR_LOWER_SHOW,
        'content': static_content(settings.SIDEBAR_LOWER_TEXT, settings.SIDEBAR_LOWER_RENDER_MODE),
        'wrap': not settings.SIDEBAR_LOWER_DONT_WRAP,
        'blockid': 'sidebar-lower'
    }

@register.inclusion_tag('sidebar/recent_tags.html')
def recent_tags():
    return {'tags': Tag.active.order_by('-id')[:settings.RECENT_TAGS_SIZE]}

@register.inclusion_tag('question_list/related_tags.html')
def question_list_related_tags(questions):
    if len(questions):
        tags = Tag.objects.filter(nodes__id__in=[q.id for q in questions]).distinct()

        if settings.LIMIT_RELATED_TAGS:
            tags = tags[:settings.LIMIT_RELATED_TAGS]

        return {'tags': tags}
    else:
        return {'tags': False}
    