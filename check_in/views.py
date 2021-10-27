from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentMeeting, Student
from django.views import generic
from . import forms, models
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.dates import WeekArchiveView
from check_in.buzz_request import BuzzRequest


# Create your views here.
def ae_login(request):  #not used??
    user = None
    if request.user.is_authenticated:
        user = request.user
    if request.POST.get(username) != None and request.POST.get(password) != None:
        buzz = BuzzRequest(user)
        buzz.login(request.username, request.password)
        return render(request, 'check_in/AE_Login.html', {'title': 'AE_Login'})

def ae_login_form(request):
    return render(request, 'check_in/AE_Login_form.html', {'title': 'AE_Login'})

def about(request):
    return render(request, 'check_in/about.html', {'title': 'About'})


def home(request):
    return render(request, 'check_in/home.html', {'title': 'Home'})


class Data(generic.ListView):
    """List of students with links to each student"""
    model = Student


class StudentDetailView(generic.DetailView):
    """List of student meetings for selected student"""
    model = Student


class MeetingWeekArchiveView(WeekArchiveView):
    """This view is used to view all meetings in a week"""
    queryset = StudentMeeting.objects.all()
    date_field = "appointment_date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name = 'check_in/meeting_archive_week.html'

    def get_context_data(self, **kwargs):
        context = super(MeetingWeekArchiveView, self).get_context_data(**kwargs)
        context['student'] = Student.objects.all()
        return context


class StudentMeetingView(SuccessMessageMixin, generic.CreateView):
    model = models.StudentMeeting
    form_class = forms.StudentMeetingForm
    template_name = 'check_in/student_meeting_form.html'
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





