from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserProfileForm, UserForm, ProfileForm



def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # username = form.cleaned_data('username')
            # password = form.cleaned_data('password1')

            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('login')

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():

        user = form.get_user()
        if user:
            print(request.POST)
            login(request, user)
            return redirect('home')

    
    return render(request, 'users/user_login.html', {"form":form} )


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html') 

def profile(request):
    form_user = ProfileForm(instance=request.user)
    form_profile = UserProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form_user = ProfileForm(request.POST, instance=request.user)
        form_profile = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('profile')
    
    context = {
        "form_user": form_user,
        "form_profile": form_profile,
    }

    return render(request, 'users/profile.html',context)