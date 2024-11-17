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
    selected_cert = query_set.filter(cct_serial_no__gt=0).order_by('cct_serial_no')
    query_set = query_set.all()
    cert_type = []
    selected_cert = selected_cert[:visible_items]
    for crt_item in query_set:
        for crt in crt_item.CERTIFICATION_TYPE_CHOICES:
            if crt not in cert_type:
                cert_type.append(crt)
    # print('cert_type ----->', cert_type, type(cert_type), selected_cert.count())
    return {'cert_type': cert_type, 'selected_cert': selected_cert}


@register.simple_tag
def get_certifications_courses_trainings_one_cert_types_and_corrected_image_url(crt_item, trim_loc='/myresources'):
    cert_types = []
    image_url = str(crt_item.cct_image)
    start_index = image_url.find(trim_loc)
    image_url = image_url[start_index:] if start_index != -1 else image_url

    for ct in crt_item.cct_type:
        cert_types.append(ct)
    # print('cert_type ----->', cert_types, type(cert_types), image_url)
    return {'cert_types': cert_types, 'image_url': image_url}


@register.simple_tag
def get_key_info_icon(ki_names):
    name_keys = ['teaching', 'software industry', 'research project', 'research publication', 'research institute', 'development industry', 'research collaboration', 'certification']
    icon_list = ["bx bi-puzzle", "bx bi-file-earmark-code", "bx bi-lightbulb", "bx bi-journal-richtext", "bx bi-building", "bx bi-tools", "bx bi-snow3", "bx bi-journal-bookmark-fill"]
    ki_names = ki_names.lower()
    icon_to_return = ''
    for i, name in enumerate(name_keys):
        if name in ki_names:
            icon_to_return = icon_list[i]
            break
    # print('----->', ki_names, icon_to_return)
    return icon_to_return


@register.simple_tag
def get_key_info_formated_description(ki_desc, hash_replacer='strong'):
    parts = ki_desc.split('#', 2)
    # If there are at least two '#' characters
    if len(parts) > 2:
        return f"{parts[0]}<{hash_replacer}>{parts[1]}</{hash_replacer}>{parts[2]}"
    return ki_desc


def divide_into_groups(d):
    # Sort dictionary by values in descending order
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

    # Initialize two groups
    group1 = {}
    group2 = {}

    sum_group1 = 0
    sum_group2 = 0

    # Greedy approach: add each item to the group with the smaller sum
    for key, value in sorted_items:
        if sum_group1 <= sum_group2:
            group1[key] = value
            sum_group1 += value
        else:
            group2[key] = value
            sum_group2 += value

    return group1, group2

@register.simple_tag
def get_category_wise_publications(publications, cols=2):
    pub_cat_seq = ['Journal', 'Conference', 'Poster', 'Blog']
    cat_groups = [['Journal'], ['Conference', 'Poster'], ['Blog']]
    pub_cats = []
    pub_cats_list = {}
    all_pubs = publications.all()

    for pub in all_pubs:
        if pub.pub_type not in pub_cats:
            pub_cats.append(pub.pub_type)
            pub_cats_list[pub.pub_type] = []
        pub_cats_list[pub.pub_type].append(pub)

    # sort publication based on cat seq
    sorted_cat = sorted(pub_cats, key=lambda x: pub_cat_seq.index(x))
    sorted_pub = {key: pub_cats_list[key] for key in pub_cat_seq if key in pub_cats_list}

    # sort publication based on number of items
    num_items_per_cat = {cc:len(sorted_pub[cc]) for cc in sorted_cat}
    sorted_num_items_per_cat = dict(sorted(num_items_per_cat.items(), key=lambda item: item[1], reverse=True))
    sorted_cat = sorted(sorted_cat, key=lambda x: list(sorted_num_items_per_cat.keys()).index(x))
    sorted_pub = {key: pub_cats_list[key] for key in list(sorted_num_items_per_cat.keys()) if key in pub_cats_list}

    group1, group2 = divide_into_groups(sorted_num_items_per_cat)
    group1, group2 = {cc:vv for cc,vv in sorted_pub.items() if cc in group1.keys()}, {cc:vv for cc,vv in sorted_pub.items() if cc in group2.keys()}
    print('sorted_cat ----->', sorted_cat, sorted_num_items_per_cat, sorted_pub, group1, group2)

    to_return = {'pub_cats': sorted_cat, 'pub_cats_list': sorted_pub, 'cat_groups': cat_groups, 'group1': group1, 'group2': group2}
    return to_return


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def get_formatted_citation(citation):
    tmp_citation = citation.split('.')
    my_name_list = ['Emran Ali', 'Emran A', 'Ali Emran', 'E Ali', 'Ali E', 'E. Ali', 'Ali E.', 'Ali, E']
    st_indx = 0
    end_indx = 0
    for my_name in my_name_list:
        # print('000', my_name, ' || ', tmp_citation[0], ' || ', tmp_citation[0].title().find(my_name))
        if tmp_citation[0].title().find(my_name) >= 0:
            print('---', my_name)
            st_indx = tmp_citation[0].title().find(my_name)
            end_indx = st_indx + len(my_name)
            break
    for i,c in enumerate(tmp_citation):
        if i==0:
            tmp_citation[i] = f"{c[:st_indx]}<strong>{c[st_indx:end_indx]}</strong>{c[end_indx:]}"
        elif i==1:
            tmp_citation[i] = f"<em>{c}</em>"
        else:
            tmp_citation[i] = c
    formatted_citation = '.'.join(tmp_citation)
    print('----->', 'citation', citation, formatted_citation)
    return formatted_citation


@register.filter
def first_item(queryset):
    return queryset.first()




