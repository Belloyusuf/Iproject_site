from django import template
from ..models import Project, Category

register = template.Library()

@register.simple_tag()
def total_project():
    return Project.objects.filter(available=True).count()


