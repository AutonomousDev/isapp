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


class PostDetailView(DetailView):
    """This view shows a single post. if the user is the author the template has
    update and delete buttons"""
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """This view is used for creating new posts."""
    model = Post
    fields = ['title', 'content', 'project']

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view is used for updating posts"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make updates"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = Post
    success_url = '/'

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make deletes"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False