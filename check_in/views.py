from django.shortcuts import render, redirect
from .models import StudentMeeting, Student, CourseEnrollment, School
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from . import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.dates import WeekArchiveView
from check_in.buzz_request import BuzzRequest
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


# Create your views here.
def ae_login(request):  #
    """Used to process the Accelerate Ed login post after hitting submit"""
    user = None
    context = {}
    if request.user.is_authenticated:
        user = request.user
        context = {
            "message": "You are signed in",
            "data": user,
            'title': 'AE_Login'
        }

    else:  # This error message has to do with an unauthenticated user signing into AE with valid credentials.
        # TODO Prevent this from happening initally with authentication checks.
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
        return render(request, 'check_in/ae_login.html', context)


def ae_login_form(request):
    """This view is used to authenticate to Accelerate Ed"""
    schools = School.objects.all()
    context = {
        'schools': schools,
        'title': 'AE_Login'
    }
    return render(request, 'check_in/ae_login_form.html', context)


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



class StudentMeetingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentMeeting
    form_class = forms.StudentMeetingForm

    success_url = '/student_meeting/new/'
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
    model = StudentMeeting


class StudentMeetingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    """This view is used for updating posts"""
    model = StudentMeeting
    template_name = "check_in/studentmeeting_update.html"
    fields = [
        'appointment_date',
        'attended_meeting',
        'missing_work_amount',
        'narrative',
    ]
    success_message = "Meeting has been updated!"

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.instructor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make updates"""
        post = self.get_object()
        if self.request.user == post.instructor:
            return True
        else:
            return False


class StudentMeetingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = StudentMeeting
    success_url = '/'


    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make deletes"""
        student_meeting = self.get_object()
        if self.request.user == student_meeting.instructor:
            return True
        else:
            return False


def manage_students(request):
    """This page is a menu of student management options"""
    return render(request, 'check_in/ae_login_form.html', {'title': 'AE_Login'})


def pre_create_student(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        token = user.profile.ae_token
    else:
        context = {
            "message": "user is none",
            "data": user
        }
        return render(request, 'debug.html', context)

    buzz = BuzzRequest(user, token)
    response = buzz.get_enrollments()


    #TODO some logic for expired token.

    return render(request, 'check_in/pre_create_student.html', {'title': "Make Student", "data": response})
