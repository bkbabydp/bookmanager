# -*- coding: UTF-8 -*-


from django import template

register = template.Library()


@register.simple_tag()
def ratio(this_value, this_max, new_max):
    return round(float(this_value) / float(this_max) * float(new_max), 2)
