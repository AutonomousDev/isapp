from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Course(models.Model):
    """Model representing courses"""
    course_name = models.CharField(max_length=200, help_text="Enter the name of the course.")
    course_id = models.CharField(max_length=200, help_text="Enter the course id code if applicable.", blank=True, default='')
    course_provider = models.ForeignKey('CourseProvider', on_delete=models.SET_NULL, null=True,  blank=True, default='')

    class Meta:
        ordering = ['course_name']

    def __str__(self):
        """String representing the Model object"""
        return f'{self.course_name}'


class CourseProvider(models.Model):
    """Model representing course providers"""
    provider_name = models.CharField(max_length=200, help_text="Enter the course provider name.")
    provider_website = models.CharField(max_length=255, help_text="Enter the course providers website.", blank=True, default='')
    lms = models.CharField(max_length=610, help_text="Enter the learning management systems web address", blank=True, default='')

    def __str__(self):
        """String representing the Model object"""
        return self.provider_name


class Student(models.Model):
    """Model representing a student"""
    first_name = models.CharField(max_length=50, help_text="Student first name.")
    last_name = models.CharField(max_length=50, help_text="Student last name.")
    course = models.ManyToManyField(Course, help_text="Select courses student is enrolled in.", null=True, blank=True, default='')

    def __str__(self):
        """String representing the Model object"""
        return self.last_name + ", " + self.first_name

    def get_absolute_url(self):
        """Returns the url to access a detailed record for this student"""
        return reverse("checkin-student-detail", args=[str(self.id)])


class StudentMeeting(models.Model):
    """Model representing a check-in appointment"""

    instructor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default='')
    student = models.ForeignKey(Student, help_text="Student Name.", on_delete=models.CASCADE, null=True)
    appointment_date = models.DateField("Date", default=timezone.now)
    attended_meeting = models.BooleanField()
    narrative = models.TextField(blank=True, default='')

    def __str__(self):
        """String representing the Model object"""
        return str(self.appointment_date) + ": " + self.student.last_name + ", " + self.student.first_name



