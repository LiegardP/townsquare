# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', default=None, null=True)
    def __str__(self):
        return self.first_name + "" + self.last_name

class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus')
    job = models.ForeignKey('Job')
    def __str__(self):
        return self.last_name

class Student(Person):
    cursus = models.ForeignKey('Cursus')
    year = models.IntegerField()        
    def __str__(self):
        return self.last_name

class Message(models.Model):
    author = models.ForeignKey('Person')
    content = models.TextField()
    publication_date = models.DateField()
    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:    
            return self.content

class Faculty(models.Model):
    name = models.CharField(max_length=30)    
    color = models.CharField(max_length=10)    
    def __str__(self):
        return self.name

class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Cursus(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
