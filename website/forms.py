from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.validators import EmailValidator

class NewsletterForm(forms.Form):
    newsletter_email = forms.EmailField(
        # label='Email',
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'youremail@mail.com', 'max_length': 200}),
        required=True, error_messages={'invalid': 'Invalid email address.'},
        validators=[EmailValidator('Invalid email address.')]
    )
    # newsletter_email = forms.EmailField(label='youremail@mail.com', required=True, validators=[validators.EmailValidator()])

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
        max_length=100
    )
    contact_email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'youremail@mail.com'}),
        required=True,
        error_messages={'invalid': 'Invalid email address.'},
        validators=[EmailValidator('Invalid email address.')]
    )
    contact_message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Message', "rows": "5"})
    )
    # contact_email = forms.EmailField(label='youremail@mail.com', required=True, validators=[validators.EmailValidator()])




