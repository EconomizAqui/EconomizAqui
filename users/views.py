from django.shortcuts import render, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordResetForm

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def settings(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user = form.save()
            return HttpResponseRedirect(reverse('home_page'))
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'settings.html', {'form': form})


def delete_user(request):
    user = CustomUser.objects.filter(username=request.user.username)
    user.delete()

    return HttpResponseRedirect(reverse('logout'))


def list_users(request):
    users = CustomUser.objects.filter(is_active=True)

    return render(request, 'list_users.html', {'users': users})

