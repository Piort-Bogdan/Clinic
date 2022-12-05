from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm


def user_login(request, form=None):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if  form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html',{'form':form
                                                      })


class RegisterUser(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('thanks')
    template_name = 'registration/register.html'

    def post(self, request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/thanks/')
            else:
                form = RegisterForm()




def ThanksPage(request):
    return HttpResponse("Спасибо за регистрацию!")
