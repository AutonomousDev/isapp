from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.student_contact, name='check-in-student_contact'),
    path('about/', views.about, name='check-in-about'),
    path('', views.home, name='check-in-home')
]
