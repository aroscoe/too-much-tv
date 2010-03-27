from django import template

from shows.models import Show

register = template.Library()

@register.inclusion_tag('shows/tags/show_list.html')
def show_list():
    shows = Show.objects.all().order_by('name')
    return {'shows': shows}