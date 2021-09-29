from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from checkin.views import MeetingWeekArchiveView
import datetime


urlpatterns = [
    path('about/', views.about, name='checkin-about'),
    path('', views.home, name='checkin-home'),
    path('data/', login_required(views.Data.as_view()), name='checkin-data'),
    path('student/<int:pk>', login_required(views.StudentDetailView.as_view()), name='checkin-student-detail'),
    path('student_meeting/', login_required(views.StudentMeetingView.as_view()), name='checkin-student-meeting'),
    path('archive/<int:year>/week/<int:week>/', MeetingWeekArchiveView.as_view(), name="checkin-meeting-archive-week"),
    path('archive/' + str(datetime.date.today().year) + '/week/'+ str(datetime.date.today().strftime("%V")) + '/', MeetingWeekArchiveView.as_view(), name="checkin-meeting-archive-week-today"),

]
