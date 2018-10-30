from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from django.urls import include


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.settings, name='settings'),
    path('password_reset/', auth_views.PasswordResetView.as_view()),
]