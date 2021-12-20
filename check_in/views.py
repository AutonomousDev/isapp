from django.shortcuts import render, redirect
from .models import StudentMeeting, Student, CourseEnrollment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from . import forms, models
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.dates import WeekArchiveView
from check_in.buzz_request import BuzzRequest
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def ae_login(request):  # Used to process the login post
    user = None
    if request.user.is_authenticated:
        user = request.user
    else:
        context = {
            "message": "user is none",
            "data": user
        }
        return render(request, 'debug.html', context)
    if request.POST.get('username') != None and request.POST.get('password') != None:
        buzz = BuzzRequest(user)
        if buzz.login(request.POST.get('username'), request.POST.get('password'), request.POST.get('school')) == 'InvalidCredentials':
            messages.error(request, f'Invalid username or password: ')
            return redirect('check_in-ae_login_form')
        return render(request, 'check_in/ae_login.html', {'title': 'AE_Login'})

def ae_login_form(request):
    return render(request, 'check_in/ae_login_form.html', {'title': 'AE_Login'})

def about(request):
    return render(request, 'check_in/about.html', {'title': 'About'})


def home(request):
    return render(request, 'check_in/home.html', {'title': 'Home'})


class StudentListView(LoginRequiredMixin, ListView):
    """List of students with links to each student"""
    model = Student
    ordering = ['last_name', 'first_name']


class StudentDetailView(LoginRequiredMixin, DetailView):
    """List of student meetings for selected student"""
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['student_meetings'] = StudentMeeting.objects.filter(student=self.get_object()).order_by('appointment_date')
        context['course_enrollments'] = CourseEnrollment.objects.filter(student=self.get_object()).order_by('course')
        return context


class MeetingWeekArchiveView(LoginRequiredMixin, WeekArchiveView):
    """This view is used to view all meetings in a week"""
    queryset = StudentMeeting.objects.all().order_by('appointment_date')
    date_field = "appointment_date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name = 'check_in/meeting_archive_week.html'

    def get_context_data(self, **kwargs):
        context = super(MeetingWeekArchiveView, self).get_context_data(**kwargs)
        context['student'] = Student.objects.all().order_by('last_name', 'first_name')
        return context


class StudentMeetingView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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


class StudentMeetingDetailView(LoginRequiredMixin, DetailView):
    """This view shows a single StudentMeeting. If the user is the author the template has
    update and delete buttons"""
    model = models.StudentMeeting
