from django.urls import path
from django.contrib.auth.decorators import login_required
import datetime
from .views import (
    #home,
    ae_login_form,
    ae_login,
    StudentListView,
    StudentDetailView,
    StudentMeetingCreateView,
    MeetingWeekArchiveView,
    StudentMeetingDetailView,
    StudentMeetingUpdateView,
    StudentMeetingDeleteView,
    manage_school
    )


urlpatterns = [
    # path('', home, name='check_in-home'), # Moved to announcements
    path('AE_login/', login_required(ae_login_form), name='check_in-ae_login_form'),
    path('AE_logged_in/', login_required(ae_login), name='check_in-ae_login'),
    path('student_list/', StudentListView.as_view(), name='check_in-data'),
    path('student/<int:pk>', login_required(StudentDetailView.as_view()), name='check_in-student-detail'),
    path('archive/<int:year>/week/<int:week>/', login_required(MeetingWeekArchiveView.as_view()), name="check_in-meeting-archive-week"),
    path('archive/' + str(datetime.date.today().year) + '/week/' + str(datetime.date.today().strftime("%V")) + '/',
         login_required(MeetingWeekArchiveView.as_view()),
         name="check_in-meeting-archive-week-today"),
    path('student_meeting/new/', StudentMeetingCreateView.as_view(), name='check_in-student-meeting'),
    path('student_meeting/<int:pk>/', StudentMeetingDetailView.as_view(), name='student_meeting-detail'),
    path('student_meeting/<int:pk>/update/', StudentMeetingUpdateView.as_view(), name='student_meeting-update'),
    path('project/<int:pk>/delete/', StudentMeetingDeleteView.as_view(), name='student_meeting-delete'),
    # path('new_student/', login_required(views.pre_create_student), name='check_in-pre_new_student'),
    path('school_manage/', manage_school, name='school-manage'),


]
