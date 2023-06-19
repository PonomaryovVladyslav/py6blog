from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AuthenticationForm
from django.contrib.auth import login, logout


def register(request):
    print('here')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "registration.html", context={'form': form})
    form = UserCreationForm(request.POST)
    return render(request, "registration.html", context={'form': form})




def user_login(request):
    # all_topics = models.Topic.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})






def username(request, username):
    return HttpResponse(f"here will be username {username}")


def change_password(request):
    return HttpResponse("here will be change_password")


# def register(request):
#     return render(request, 'registration.html')


# def login(request):
#     return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("user_login")


