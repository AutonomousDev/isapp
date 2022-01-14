from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.
class PostListView(ListView):
    """This view list all post with pagination for now it's also the home page"""
    model = Post
    template_name = 'announcements/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


