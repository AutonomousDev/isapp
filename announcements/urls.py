from django.urls import path
from django.contrib.auth.decorators import login_required
import datetime
from .views import (PostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='check_in-home'),
    ]
