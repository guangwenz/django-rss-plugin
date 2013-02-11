from datetime import datetime
from django import template
import time

register = template.Library()


@register.filter
def parsed_to_date(value):
    return datetime(*time.localtime(time.mktime(value))[:6])
