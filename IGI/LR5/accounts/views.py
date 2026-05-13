from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import RegisterForm


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


@login_required
def profile_view(request):

    return render(request, 'accounts/profile.html')

def logout_view(request):

    logout(request)

    return redirect('/')