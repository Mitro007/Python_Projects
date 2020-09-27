from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        # A form that creates a user, with no privileges, from the given username and password.
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # save the user to auth_user
            form.save()
            username = form.cleaned_data.get("username")
            # Display a flash message
            messages.success(request, f"Account created for {username}!")
            return redirect("blog_home")
    else:
        # A form that creates a user, with no privileges, from the given username and password.
        # form = UserCreationForm()
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})
