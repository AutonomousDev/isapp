from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from check_in.views import MeetingWeekArchiveView
import datetime


urlpatterns = [
    path('about/', views.about, name='check_in-about'),
    path('', views.home, name='check_in-home'),
    path('AE_login/', login_required(views.ae_login_form), name='check_in-ae_login_form'),
    path('AE_logged_in/', login_required(views.ae_login), name='check_in-ae_login'),
    path('data/', login_required(views.Data.as_view()), name='check_in-data'),
    path('student/<int:pk>', login_required(views.StudentDetailView.as_view()), name='check_in-student-detail'),
    path('student_meeting/', login_required(views.StudentMeetingView.as_view()), name='check_in-student-meeting'),
    path('archive/<int:year>/week/<int:week>/', login_required(MeetingWeekArchiveView.as_view()), name="check_in-meeting-archive-week"),

    path('archive/' + str(datetime.date.today().year) + '/week/'+ str(datetime.date.today().strftime("%V")) + '/',
         login_required(MeetingWeekArchiveView.as_view()),
         name="check_in-meeting-archive-week-today"),
    path('new_student/', login_required(views.pre_create_student), name='check_in-pre_new_student'),



]
