from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.validators import EmailValidator

class NewsletterForm(forms.Form):
    newsletter_email = forms.EmailField(label='youremail@mail.com', widget=forms.TextInput(attrs={'placeholder': 'youremail@mail.com'}),
                                        required=True, error_messages={'invalid': 'Invalid email address.'},
                                        validators=[EmailValidator('Invalid email address.')])
    # newsletter_email = forms.EmailField(label='email.address@domain.com', required=True, validators=[validators.EmailValidator()])




