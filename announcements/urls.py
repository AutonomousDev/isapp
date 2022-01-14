from django.urls import path
from django.contrib.auth.decorators import login_required
import datetime
from .views import (
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='check_in-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    ]
