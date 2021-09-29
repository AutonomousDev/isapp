from django import forms
from django_select2 import forms as s2forms

from . import models


class StudentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "last_name__icontains",
    ]


class StudentMeetingForm(forms.ModelForm):
    class Meta:
        model = models.StudentMeeting
        exclude = ["instructor"]
        fields = "__all__"
        widgets = {
            "student": StudentWidget,
        }

