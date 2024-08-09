# myproject/context_processors.py

import datetime
import random

def theme_processor_login(request):
    if request.user.is_authenticated:
        # Assume user has a 'theme' attribute
        theme = request.user.profile.theme
        # theme = 'theme2'
    else:
        theme = 'theme1'  # default theme
    return {'theme': theme}

def theme_processor_time_minutes(request):
    # current_minute = datetime.datetime.now().minute
    # theme = 'theme1' if current_minute % 2 == 1 else 'theme2'

    theme_list = ['theme1', 'theme2', 'theme3', 'theme4', 'theme5']
    # theme_list = ['theme1', 'theme2']
    selected_theme_indx = random.randint(0, len(theme_list)-1)
    selected_theme_indx = 0
    theme = theme_list[selected_theme_indx]
    return {
        'theme': theme
    }

def theme_processor_random_color(request, custom_color=None):
    current_color = request.session.get('theme_color')
    print('======>>> current_color', current_color)
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
    request.session['theme_color'] = theme_color
    return {'theme_color': theme_color}


def copyright_current_year(request):
    return {
        'current_year': datetime.datetime.now().year,
    }


