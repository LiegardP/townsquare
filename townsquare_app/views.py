# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from townsquare_app.forms import LoginForm
from townsquare_app.forms import StudentProfileForm, EmployeeProfileForms


def welcome(request):
    return render_to_response('welcome.html', {'current_date_time': datetime.now})


def login(request):
    # Test si formulaire a été envoyé
    if len(request.GET) > 0:
        form = LoginForm(request.GET)
        if form.is_valid():
            return HttpResponseRedirect('/welcome')
        else:
            return render_to_response('login.html', {'form': form})
    # Le formulaire n'a pas été envoyé
    else:
        form = LoginForm()
        return render_to_response('login.html', {'form': form})


def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForms(prefix="em")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/login')
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfileForms(request.GET, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('/login')

        return render(request, 'user_profile.html',
                      {'studentForm': studentForm,
                       'employeeForm': employeeForm})

    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForms(prefix="em")
        return render(request, 'user_profile.html',
                      {'studentForm': studentForm,
                       'employeeForm': employeeForm})
