from django import forms
from django_select2 import forms as s2forms

from . import models


class StudentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "username__icontains",
        "email__icontains",
    ]


class StudentMeetingForm(forms.ModelForm):
    class Meta:
        model = models.StudentMeeting
        fields = "__all__"
        widgets = {
            "student": StudentWidget,
        }
