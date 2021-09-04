from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def student_contact(request):
    return HttpResponse('<h1>Check in student</h1>')
