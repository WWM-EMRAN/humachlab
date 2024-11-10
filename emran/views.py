from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from .forms import NewsletterForm, ContactForm
import pprint
from .data_manager import *

# Create your views here.
def index(request):
    # pprint.pprint(request.__dict__.keys())
    # return HttpResponse(f"This is a response from 'index' page...\n{request.__dict__['META']['PATH_INFO']}")

    all_data_models = get_all_data_models()
    print(all_data_models.keys())
    return render(request, 'emran_theme1/index.html', all_data_models)

