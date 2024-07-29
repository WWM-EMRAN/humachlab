from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is a response from 'index' page...")
    # return render(request, 'index.html')
    return render(request, 'theme1/index.html')
    # return render(request, 'theme2/index.html')
    # return render(request, f'{request.context["theme"]}/index.html')


# def home(request):
#     return HttpResponse("This is a response from 'home' page...")
#     # return render(request, 'index.html')
#     return render(request, 'theme1/index.html')
#     # return render(request, 'theme2/index.html')
#     # return render(request, f'{request.context["theme"]}/index.html')


    # # path('', views.home, name='home'),
    # path('services', views.index, name='services'),
    # path('aboutus', views.index, name='aboutus'),
    # path('blog', views.index, name='blog'),
    # path('contact', views.index, name='contact'),
def services(request):
    # return HttpResponse("This is a response from 'services' page...")
    appropriate_page = None
    serv_type = request.GET['type']
    # serv_id = request.GET['id']
    print('Here we go....', serv_type)
    if serv_type == 'research':
        appropriate_page = service_research(request)
    elif serv_type == 'education':
        appropriate_page = service_research(request)
    elif serv_type == 'development':
        appropriate_page = service_research(request)
    else:
        pass

    return appropriate_page


def service_research(request):
    # page = HttpResponse("This is a response from 'services' page and 'research' service...")
    serv_type = request.GET['type']
    serv_id = request.GET['id']
    # page = render(request, 'theme1/research.html')
    page = render(request, 'theme1/research.html', {'type':serv_type, 'id':serv_id})
    return page


def service_education(request):
    # page = HttpResponse("This is a response from 'services' page and 'education' service...")
    serv_type = request.GET['type']
    serv_id = request.GET['id']
    # page = render(request, 'theme1/education.html')
    page = render(request, 'theme1/education.html', {'type':serv_type, 'id':serv_id})
    return page


def service_development(request):
    # page = HttpResponse("This is a response from 'services' page and 'development' service...")
    serv_id = request.GET['id']
    print(f'Here2: ... {serv_id}')
    # page = render(request, 'theme1/development.html')
    page = render(request, 'theme1/development.html', {'type':serv_type, 'id':serv_id})
    return page


def contact(request):
    # return HttpResponse("This is a response from 'contact' page...")
    return render(request, 'theme1/contact.html')




