from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
# from .forms import NewsletterForm, ContactForm

# Create your views here.
def index(request):
    return HttpResponse("This is a response from 'index' page...")
