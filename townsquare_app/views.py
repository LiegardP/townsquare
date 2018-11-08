# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html', {'current_date_time': datetime.now})

def login(request):
    if len(request.POST) > 0:
        if 'email' not in request.POST or 'password' not in request.POST:
            error = "Veuillez entrer une adresse et un mot de passe valide"
            return render(request, 'login.html', {'error': error})
        else:
            email = request.POST['email']
            password = request.POST['password']

            if password != 'sesame' or email != 'toto@test.com':
                error = "Adresse de courriel ou mot de passe erroné"
                return render(request, 'login.html', {'error': error})
            else:
                return redirect('/welcome')
    else:
        return render(request, 'login.html')