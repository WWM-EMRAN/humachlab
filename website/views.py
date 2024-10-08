from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .forms import NewsletterForm, ContactForm

# Create your views here.
def index(request):
    # return HttpResponse("This is a response from 'index' page...")
    # return render(request, 'index.html')
    # form_newsletter = NewsletterForm()
    # return render(request, 'theme1/index.html', {'form_newsletter': form_newsletter})
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
    if request.GET:
        serv_type = request.GET['type']
        # serv_id = request.GET['id']
        if serv_type == 'research':
            appropriate_page = service_research(request)
        elif serv_type == 'education':
            appropriate_page = service_education(request)
        elif serv_type == 'development':
            appropriate_page = service_development(request)
        else:
            appropriate_page = service_all(request)
    else:
        appropriate_page = service_all(request)

    return appropriate_page


def service_all(request):
    # page = HttpResponse("This is a response from 'services' page and 'all' service...")
    # page = render(request, 'theme1/research.html')
    page = render(request, 'theme1/services.html')
    return page


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
    serv_type = request.GET['type']
    serv_id = request.GET['id']
    # page = render(request, 'theme1/development.html')
    page = render(request, 'theme1/development.html', {'type':serv_type, 'id':serv_id})
    return page


def news(request):
    # return HttpResponse("This is a response from 'news' page...")
    return render(request, 'theme1/news.html')


def news_details(request):
    news_id = request.GET['news_id']
    # return HttpResponse("This is a response from 'news' page...")
    return render(request, 'theme1/news_details.html', {'news_id': news_id})


def contact(request):
    # return HttpResponse("This is a response from 'contact' page...")
    return render(request, 'theme1/contact.html')


def form_contact(request):
    # return HttpResponse("This is a response from 'contact_form_processing' page...")
    # return render(request, 'theme1/contact_form_processing.html')
    if request.POST:
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']

        page_name = "Contact"
        if contact_email:
            message = f"Your ({contact_name}-{contact_email}) message is successfully sent."
            return render(request, 'theme1/_success_page.html', {'page_name': page_name, 'message': message})
        else:
            message = f"Invalid email adress ({contact_name}-{contact_email}) entered for the contact message."
            return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'message': message})
    else:
        page_name = "Contact"
        error_tag = 404 #"Error"
        message = f"Invalid method for email adress submission for the contact message."
        return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'error_tag': error_tag, 'message': message})

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Process the data in form.cleaned_data
    #         contact_name = request.POST['contact_name']
    #         contact_email = request.POST['contact_email']
    #         contact_message = request.POST['contact_message']
    #         return render(request, 'theme1/_success_page.html', {'contact_name': contact_name, 'contact_email': contact_email, 'contact_message': contact_message})

    return redirect('/index')
    # return HttpResponseRedirect(request, 'theme1/index.html')
    # return render(request, 'theme1/index.html')


def form_search(request):
    # return HttpResponse("This is a response from 'newsletter' page...")
    # return render(request, 'theme1/_success_page.html')
    if request.POST:
        search_query = request.POST['search_query']

        page_name = "Search"
        if search_query:
            return render(request, 'theme1/search_result.html', {'page_name': page_name, 'search_query': search_query})
            # return render(request, 'theme1/_success_page.html', {'page_name': page_name, 'search_query': search_query})
        else:
            message = f"No result found for '{search_query}'"
            return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'message': message})
    else:
        page_name = "Search"
        error_tag = 404 #"Error"
        message = f"Invalid method for email adress submission for the newsletter."
        return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'error_tag': error_tag, 'message': message})

    # if request.method == 'POST':
    #     form = NewsletterForm(request.POST)
    #     if form.is_valid():
    #         # Process the data in form.cleaned_data
    #         newsletter_email = form.cleaned_data['newsletter_email']
    #         return render(request, 'theme1/_success_page.html', {'newsletter_email': newsletter_email})

    return redirect('/index')
    # return HttpResponseRedirect(request, 'theme1/index.html')
    # return render(request, 'theme1/index.html')


def form_newsletter(request):
    # return HttpResponse("This is a response from 'newsletter' page...")
    # return render(request, 'theme1/_success_page.html')
    if request.POST:
        newsletter_email = request.POST['newsletter_email']

        page_name = "Newsletter"
        if newsletter_email:
            message = f"Your email ({newsletter_email}) is successfully registered for the newsletter."
            return render(request, 'theme1/_success_page.html', {'page_name': page_name, 'message': message})
        else:
            message = f"Invalid email adress ({newsletter_email}) entered for the newsletter."
            return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'message': message})
    else:
        page_name = "Newsletter"
        error_tag = 404 #"Error"
        message = f"Invalid method for email adress submission for the newsletter."
        return render(request, 'theme1/_unsuccess_page.html', {'page_name': page_name, 'error_tag': error_tag, 'message': message})

    # if request.method == 'POST':
    #     form = NewsletterForm(request.POST)
    #     if form.is_valid():
    #         # Process the data in form.cleaned_data
    #         newsletter_email = form.cleaned_data['newsletter_email']
    #         return render(request, 'theme1/_success_page.html', {'newsletter_email': newsletter_email})

    return redirect('/index')
    # return HttpResponseRedirect(request, 'theme1/index.html')
    # return render(request, 'theme1/index.html')


def under_construction(request):
    page_name = "Under Construction"
    error_tag = "Under Construction!"
    message = f"The website is coming soon!"
    return render(request, 'theme1/under_construction.html', {'page_name': page_name, 'error_tag': error_tag, 'message': message})


def set_custom_color(request):
    return render(request, 'theme1/index.html')





