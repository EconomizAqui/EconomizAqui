from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.settings, name='settings')
]