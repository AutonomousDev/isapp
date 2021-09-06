from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentMeeting


# Create your views here.
def student_contact(request):
    return render(request, 'checkin/student_contact.html')


def about(request):
    return render(request, 'checkin/about.html', {'title': 'About'})


def home(request):
    return render(request, 'checkin/home.html', {'title': 'Home'})

def data(request):
    context = {
        'meetings': StudentMeeting.objects.all()
    }
    return render(request, 'checkin/data_summary.html', context)

