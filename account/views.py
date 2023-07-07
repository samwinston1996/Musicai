from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    # Check if the user is already authenticated, redirect them to the home page
    if request.user.is_authenticated:
        return redirect("home")

    # Handle the form submission when the method is POST
    if request.method == "POST":
        # Create a RegisterForm instance with the POST data
        form = RegisterForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user and log them in
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            # If the form is invalid, iterate over the form fields and collect the error messages
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            # Redirect the user back to the registration page
            return redirect("register")

    # If the method is not POST, create an empty RegisterForm instance
    form = RegisterForm()
    # Render the registration template with the form as context
    return render(request, "account/register.html", {"form": form})



def login_page(request):
    # Check if the user is already authenticated, redirect them to the home page
    if request.user.is_authenticated:
        return redirect("home")

    # Handle the form submission when the method is POST
    if request.method == "POST":
        # Get the username and password from the form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if the "remember_me" checkbox is checked
        remember_me = request.POST.get("remember_me") == "on"
        # Authenticate the user with the provided credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # If the user is authenticated, log them in
            if remember_me:
                # If "remember_me" is checked, set the session expiry to 2 weeks (1209600 seconds)
                login(request, user)
                request.session.set_expiry(1209600)
            else:
                # If "remember_me" is not checked, log in the user without setting session expiry
                login(request, user)
            # Redirect the user to the home page
            return redirect("home")
        else:
            # If the provided credentials are invalid, display an error message
            messages.error(request, "Invalid username or password!")
            # Redirect the user back to the login page
            return redirect("login")

    # If the method is not POST, render the login template
    return render(request, "account/login.html")



# logout handler
@login_required
def logout_page(request):
    logout(request)
    return redirect("login")