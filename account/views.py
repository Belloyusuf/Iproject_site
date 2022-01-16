from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# from django.core.mail import send_mail

# Authentication form
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('authenticated')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Activations')

    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})
    