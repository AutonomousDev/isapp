from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.student_contact, name='checkin-student_contact'),
    path('about/', views.about, name='checkin-about'),
    path('', views.home, name='checkin-home'),
    path('data/', views.data, name='checkin-data')
]
