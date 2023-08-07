from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from bloggin.models import Blogpost, Topic, Comment


class Login(LoginView):
    success_url = reverse_lazy('user_login')
    template_name = 'login.html'

    def get_success_url(self):
        return self.success_url


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('blogs')


class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('user_login')
    login_url = 'logout/'


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('blogs')


class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blogpost.objects.filter(author=self.request.user).order_by('updated_at')
        context['followers'] = Topic.objects.filter(followers=True).order_by('updated_at')
        context['likes'] = Blogpost.objects.filter(likes=True).order_by('updated_at')
        context['dislikes'] = Blogpost.objects.filter(dislikes=True).order_by('updated_at')
        context['comments'] = Comment.objects.filter(author=self.request.user).order_by('updated_at')
        return context





