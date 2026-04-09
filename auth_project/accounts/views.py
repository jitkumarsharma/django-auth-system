from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomSetPasswordForm

# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


# LOGIN (EMAIL आधारित)
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'password_reset_confirm.html'