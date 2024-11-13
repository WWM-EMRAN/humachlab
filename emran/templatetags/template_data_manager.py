from django import template
from django.conf import settings
import math



register = template.Library()


@register.simple_tag
def get_skills_and_tools_rows_counter(tot_items, cols=2):
    rows = math.ceil(tot_items / cols)
    print('Data sent ----->', tot_items, cols, '\nReturn value ----->', rows)
    return rows


@register.simple_tag
def get_skills_and_tools_query_subset(query_set, cols=2):
    query_set = query_set.all()
    tot_items = query_set.count()
    rows = math.ceil(tot_items / cols)
    print('Data sent ----->', tot_items, cols, '\nReturn value ----->', rows)
    query1 = query_set[:rows]
    query2 = query_set[rows:]
    return {'skltl1': query1, 'skltl2': query2}

