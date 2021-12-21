from django.contrib import admin

# Register your models here.
from .models import Course, CourseProvider, Student, StudentMeeting, CourseEnrollment, School

admin.site.register(Course)
admin.site.register(CourseProvider)
admin.site.register(Student)
admin.site.register(StudentMeeting)
admin.site.register(CourseEnrollment)
admin.site.register(School)
