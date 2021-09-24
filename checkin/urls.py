from django.urls import path
from . import views


urlpatterns = [
    path('form/', views.student_contact, name='checkin-student_contact'),
    path('about/', views.about, name='checkin-about'),
    path('', views.home, name='checkin-home'),
    path('data/', views.Data.as_view(), name='checkin-data'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='checkin-student-detail'),
    path('student_meeting/', views.StudentMeetingView.as_view(), name='checkin-student-meeting'),

]
