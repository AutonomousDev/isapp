from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentMeeting, Student
from django.views import generic
from . import forms, models
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def student_contact(request):
    """Depreciated use StudentMeetingView. TODO Phase out"""
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


class StudentDetailView(generic.DetailView):
    model = Student


class StudentMeetingView(SuccessMessageMixin, generic.CreateView):
    model = models.StudentMeeting
    form_class = forms.StudentMeetingForm
    template_name = 'checkin/student_meeting_form.html'
    success_url = '/student_meeting/'
    success_message = "%(student)s's Meeting recorded"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            this_student=self.object.student,
        )

    def form_valid(self, form):
        student_meeting = form.save(commit=False)
        student_meeting.instructor = self.request.user
        student_meeting.save()
        return super().form_valid(form)



