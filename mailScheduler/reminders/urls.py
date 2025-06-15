from django.urls import path
from .views import home, add_reminder
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_reminder, name='add_reminder'),
    path('login/', auth_views.LoginView.as_view(template_name='reminders/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]