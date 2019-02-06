# -*- coding: utf-8 -*-

from django import forms
from townsquare_app.models import Person, Student, Employee

class LoginForm(forms.Form):
  	email = forms.EmailField(label='Courriel :')
  	password = forms.CharField(label='Mot de passe :', 
                               widget = forms.PasswordInput)
	result = ''
							   
  	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		email = cleaned_data.get("email")
		password = cleaned_data.get("password")
		
		# Vérifie que les deux champs sont valides
		if email and password:
			result = Person.objects.filter(password=password,
										email=email)
		if len(result) != 1:
			raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")
	
		return cleaned_data

class StudentProfileForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ('friends',)

class EmployeeProfileForms(forms.ModelForm):
	class Meta:
		model = Employee
		exclude = ('friends',)
