from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_contact, name='check-in-student_contact'),
]
