from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView

class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "users/login.html"
    def get_success_url(self):
        return reverse_lazy("todos:list")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")