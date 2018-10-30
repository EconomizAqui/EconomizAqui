from django.shortcuts import render, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordResetForm

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm


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