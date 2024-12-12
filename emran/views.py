from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
# from .forms import NewsletterForm, ContactForm
import pprint
import json
from django.template import RequestContext
from .data_manager import *
from emran.context_processor import *


# Create your views here.
def index(request):
    context = theme_processor(request)
    emran_theme = context['emran_theme']

    # pprint.pprint(request.__dict__.keys())
    # return HttpResponse(f"This is a response from 'index' page...\n{request.__dict__['META']['PATH_INFO']}")

    # print(emran_theme, request.__dict__)
    all_data_models = get_all_data_models(page='home')
    # print(all_data_models.keys(), all_data_models.values(), all_data_models)
    # print(emran_theme, all_data_models.keys())

    # return render(request, 'emran_theme1/index.html', all_data_models)
    return render(request, f'{emran_theme}/index.html', all_data_models)


def details(request):
    context = theme_processor(request)
    emran_theme = context['emran_theme']

    # pprint.pprint(request.__dict__.keys())
    get_all_data = {k:v for k,v in request.GET.items()}
    all_data = {k:v for k,v in request.POST.items()}
    for k,v in get_all_data.items():
        all_data[k] = v

    # for k,v in all_data.items():
    #     print('All data--->', k, type(v), v)
    # print(all_data.keys(), all_data.values(), all_data, get_all_data)

    # return render(request, 'emran_theme1/details.html', all_data)
    return render(request, f'{emran_theme}/details.html', all_data)


def contacts(request):
    # pprint.pprint(request.__dict__.keys())
    get_all_data = {k:v for k,v in request.GET.items()}
    all_data = {k:v for k,v in request.POST.items()}
    for k,v in get_all_data.items():
        all_data[k] = v
    # for k,v in all_data.items():
    #     print('All data--->', k, type(v), v)
    print('All data--->', all_data.keys(), all_data.values(), all_data, get_all_data)

    if not all(all_data.values()):
        return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

    # Save to database or perform other actions
    try:
        # Save logic here, e.g., create a new model instance
        # Example: MyModel.objects.create(name=name, email=email, subject=subject, message=message)
        return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An error occurred while saving the data.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
    # return render(request, f'{emran_theme}/contacts.html', all_data)


def test(request):
    context = theme_processor(request)
    emran_theme = context['emran_theme']
    return render(request, f'{emran_theme}/test.html')





