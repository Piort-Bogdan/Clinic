from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


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


def RegisterUser(request, reg_form=None):

    if request.method == "POST":
        reg_form = RegisterForm(request.POST)
        return HttpResponse('Регистрация')
    return render(request, 'registration/register.html', {'reg_form':reg_form
                                                        })

