from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class CourseProvider(models.Model):
    """Model representing course providers"""
    provider_name = models.CharField(max_length=200, help_text="Enter the course provider name.")
    provider_website = models.CharField(max_length=255, help_text="Enter the course providers website.", blank=True, default='')
    lms = models.CharField(max_length=610, help_text="Enter the learning management systems web address", blank=True, default='')

    def __str__(self):
        """String representing the Model object"""
        return self.provider_name


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


class School(models.Model):
    """This model is used to help with API call to Accelerate Ed"""
    name = models.CharField(max_length=100, help_text="Name of the school")
    ae_subdomain = models.CharField(max_length=200, default="", blank=True,
                                    help_text="Enter the subdomain of the accelerate ed site. Ex: 'hogwarts.agilixbuzz.com' would be 'hogwarts'.")
    ae_domainid = models.CharField(max_length=20, default="", blank=True, help_text="This value is used to make API calls to accelerate ed. Leave blank if your not sure.")

    def __str__(self):
        """String representing the Model object"""
        return self.name


class Student(models.Model):
    """Model representing a student"""
    first_name = models.CharField(max_length=50, help_text="Student first name.")
    last_name = models.CharField(max_length=50, help_text="Student last name.")
    id_number = models.CharField(max_length=10, help_text="Student ID number")
    active = models.BooleanField(help_text="Uncheck box for inactive students", default=True)
    ae_id = models.CharField(max_length=20, default="", blank=True, help_text="This value is used to link AE accounts to students.")

    def __str__(self):
        """String representing the Model object"""
        return self.last_name + ", " + self.first_name

    def get_absolute_url(self):
        """Returns the url to access a detailed record for this student"""
        return reverse("check_in-student-detail", args=[str(self.id)])


class CourseEnrollment(models.Model):
    """This model tracks what courses a student is enrolled in, start dats and end date"""
    student = models.ForeignKey(Student, help_text="Student Name.", on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, help_text="Select course student is enrolled in.", blank=True, default='', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.ForeignKey(School, help_text="Select school providing course.", on_delete=models.SET_NULL, null=True, blank=True)
    ae_id = models.CharField(max_length=20, default="", blank=True,
                             help_text="This value is used to link AE course to the app.")

    def __str__(self):
        """String representing the Model object"""
        return str(self.student) + ": " + str(self.course)


class StudentMeeting(models.Model):
    """Model representing a check-in appointment"""

    instructor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default='')
    student = models.ForeignKey(Student, help_text="Student Name.", on_delete=models.CASCADE, null=True)
    appointment_date = models.DateField("Date", default=timezone.now)
    attended_meeting = models.BooleanField()
    missing_work_amount = models.IntegerField(default=0)
    narrative = models.TextField(blank=True, default='')

    def __str__(self):
        """String representing the Model object"""
        return str(self.appointment_date) + ": " + self.student.last_name + ", " + self.student.first_name

    def get_absolute_url(self):
        """Returns a url to the detail view for the meeting"""
        return reverse('student_meeting-detail', kwargs={'pk': self.pk})










