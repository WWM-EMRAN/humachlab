# myproject/context_processors.py

import datetime

def theme_processor_login(request):
    if request.user.is_authenticated:
        # Assume user has a 'theme' attribute
        theme = request.user.profile.theme
        # theme = 'theme2'
    else:
        theme = 'theme1'  # default theme
    return {'theme': theme}

def theme_processor_time_minutes(request):
    current_minute = datetime.datetime.now().minute
    theme = 'theme1' if current_minute % 2 == 1 else 'theme2'
    return {'theme': theme}


def copyright_current_year(request):
    return {
        'current_year': datetime.datetime.now().year,
    }


