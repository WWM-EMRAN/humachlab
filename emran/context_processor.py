# myproject/context_processors.py

import datetime
import random

def theme_processor_login(request):
    if request.user.is_authenticated:
        # Assume user has a 'theme' attribute
        theme = request.user.profile.theme
        # theme = 'theme2'
    else:
        theme = 'emran_theme1'  # default theme
    print(f'---> emran-theme_processor_login-{theme}')
    return {'emran_theme': theme}

def theme_processor(request):
    # current_minute = datetime.datetime.now().minute
    # theme = 'theme1' if current_minute % 2 == 1 else 'theme2'

    theme_list = ['emran_theme1', 'emran_theme2', 'emran_theme3', 'emran_theme4', 'emran_theme5']
    # theme_list = ['theme1', 'theme2']
    selected_theme_indx = random.randint(0, len(theme_list)-1)
    selected_theme_indx = 0
    theme = theme_list[selected_theme_indx]
    print(f'---> emran-theme_processor-{theme}')
    return {'emran_theme': theme}

def theme_processor_random_color(request, custom_color=None):
    current_color = request.session.get('theme_color')
    # print('======>>> current_color', current_color)
    color_list = ["red", "green", "black", "white", "blue", "gray", "orange", "turquoise", "yellow", "purple", "cyan"]
    color_list = ["red", "green", "black", "blue", "gray", "orange", "turquoise", "yellow", "purple", "cyan"]
    # color_list = ["red", "green", "black", "blue", "gray", "orange", "turquoise", "purple"]
    selected_color_indx = random.randint(0, len(color_list)-1)
    theme_color = color_list[selected_color_indx]
    ### set previous color if you want to keep the same color for a session (no change for refresh)
    # if current_color != None:
    #     theme_color = current_color
    # if custom_color != None:
    #     theme_color = custom_color
    request.session['emran_theme_color'] = theme_color
    print(f'---> emran-theme_processor_random_color-{theme_color}')
    return {'emran_theme_color': theme_color}


def copyright_current_year(request):
    cr_year = datetime.datetime.now().year
    print(f'---> emran-copyright_current_year-{cr_year}')
    return {'emran_current_year': cr_year}


