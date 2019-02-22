from django import template
from mylogin.models import *
register = template.Library()


@register.filter(name='comment')
def count_comments(value):
    p=comment.objects.filter(post=value).count()
    #print p
    return p