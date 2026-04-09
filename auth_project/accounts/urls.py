from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MyPasswordResetConfirmView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('forgot-password/',
         auth_views.PasswordResetView.as_view(
             template_name='forgot_password.html',
             email_template_name='password_reset_email.html',
             success_url='/reset-sent/'
         ),
         name='forgot_password'),

    path('reset-sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html',
             success_url='/reset-complete/'
         ),
         name='password_reset_confirm'),


    path('reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]