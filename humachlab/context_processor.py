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

def theme_processor_timeminutes(request):
    current_minute = datetime.datetime.now().minute
    theme = 'theme1' if current_minute % 2 == 1 else 'theme2'
    return {'theme': theme}


