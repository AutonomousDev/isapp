from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentMeeting, Student
from django.views import generic
from . import forms, models


# Create your views here.
def student_contact(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'checkin/student_contact.html', context)


def about(request):
    return render(request, 'checkin/about.html', {'title': 'About'})


def home(request):
    return render(request, 'checkin/home.html', {'title': 'Home'})


class Data(generic.ListView):
    model = Student

# def data(request):
#     context = {
#         'meetings': StudentMeeting.objects.all()
#     }
#     return render(request, 'checkin/data_summary.html', context)


class StudentDetailView(generic.DetailView):
    model = Student


class StudentMeetingView(generic.CreateView):
    model = models.StudentMeeting
    form_class = forms.StudentMeetingForm
    success_url = "/"

