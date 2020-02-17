# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm
from django.views.generic.detail import DetailView


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail View"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('created')
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:details', kwargs={'username': username})


class ClassLoginView(LoginView):
    template_name = 'users/login.html'


class SignUpView(FormView):
    """Users signup view"""
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        form.save()

        username = form['username'].value()
        password = form['password'].value()

        user = authenticate(
            self.request, username=username, password=password)

        if user:
            login(self.request, user)
            return redirect('posts:feed')
        else:
            return redirect('users:login')


class ClassLogoutView(LoginRequiredMixin, LogoutView):

    template_name='users/logout.html'
