from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()

class BWCreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('private_name','first_name','last_name')

class Signup(generic.CreateView):
    form_class = BWCreateUserForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class BWEditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('private_name', 'first_name', 'last_name')

class Profile(FormView):
    form_class = BWEditUserForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")
    pass

class Login(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("profile")

class Logout(LogoutView):
    template_name = "accounts/logout.html"
