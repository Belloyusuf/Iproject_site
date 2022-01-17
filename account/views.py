from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from projectapp.views import project_list
from django.contrib import messages

# from django.core.mail import send_mail


# user registration form
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user but don't save it
            new_user = user_form.save(commit=False)
            # set user password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            return render(request, 'register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'register.html',
                      {'user_form':user_form})


# login form
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
                    messages.add_message(request, messages.SUCCESS, 'Login successfull')
                    return redirect('comment')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Activations')

    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})
    