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
    # print('Data sent ----->', tot_items, cols, '\nReturn value ----->', rows)
    query1 = query_set[:rows]
    query2 = query_set[rows:]
    return {'skltl1': query1, 'skltl2': query2}


@register.simple_tag
def get_certifications_courses_trainings_all_cert_type(query_set, visible_items=6):
    # query_set = query_set.order_by('cct_serial_no')
    # query_set = query_set.reverse()
    # # query_set = query_set.order_by('id').reverse()
    selected_cert = query_set.filter(cct_serial_no__isnull=False).order_by('cct_serial_no')
    # null_items = query_set.filter(cct_serial_no__isnull=True)
    # query_set = non_null_items | null_items
    query_set = query_set.all()
    cert_type = []
    selected_cert = selected_cert[:visible_items]
    for crt_item in query_set:
        for crt in crt_item.CERTIFICATION_TYPE_CHOICES:
            if crt not in cert_type:
                cert_type.append(crt)
    print('cert_type ----->', cert_type, type(cert_type), selected_cert.count())
    return {'cert_type': cert_type, 'selected_cert': selected_cert}


@register.simple_tag
def get_certifications_courses_trainings_one_cert_types_and_corrected_image_url(crt_item, trim_loc='/myresources'):
    cert_types = []
    image_url = str(crt_item.cct_image)
    start_index = image_url.find(trim_loc)
    image_url = image_url[start_index:] if start_index != -1 else image_url

    for ct in crt_item.cct_type:
        cert_types.append(ct)
    print('cert_type ----->', cert_types, type(cert_types), image_url)
    return {'cert_types': cert_types, 'image_url': image_url}

