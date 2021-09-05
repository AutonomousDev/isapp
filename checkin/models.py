from django.db import models
import datetime


# Create your models here.
class Course(models.Model):
    """Model representing courses"""
    course_name = models.CharField(max_length=200, help_text="Enter the name of the course.")
    course_id = models.CharField(max_length=200, help_text="Enter the course id code if applicable.")
    course_provider = models.ForeignKey('CourseProvider', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String representing the Model object"""
        return self.course_name


class CourseProvider(models.Model):
    """Model representing course providers"""
    provider_name = models.CharField(max_length=200, help_text="Enter the course provider name.")
    provider_website = models.CharField(max_length=255, help_text="Enter the course providers website.")
    lms = models.CharField(max_length=610, help_text="Enter the learning management systems web address")

    def __str__(self):
        """String representing the Model object"""
        return self.provider_name


class Student(models.Model):
    """Model representing a student"""
    first_name = models.CharField(max_length=50, help_text="Student first name.")
    last_name = models.CharField(max_length=50, help_text="Student last name.")
    course = models.ManyToManyField(Course, help_text="Select courses student is enrolled in.")

    def __str__(self):
        """String representing the Model object"""
        return self.last_name + ", " + self.first_name

    def get_absolute_url(self):
        """Returns the url to access a detailed record for this student"""
        return reversed("student-detail", args=[str(self.id)])


class StudentMeeting(models.Model):
    """Model representing a check-in appointment"""
    appointment_date = models.DateField("Date", default=datetime.date.today)
    attended_meeting = models.BooleanField()


#Multiple choice isn't working todo
    # MISSING_WORK_CHOICES = (
    #     (0, "Caught up on work")
    #     (1, "1 missing assignment")
    #     (2, "2 missing assignment")
    #     (3, "3+ missing assignment")
    # )




