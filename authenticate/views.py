from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def loginview(request):
    message = ""
    # if this is a POST request we need to process the login attempt
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # get username and password submitted
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # get ip for recording login
            ip = request.META.get('REMOTE_ADDR')

            # if the user exists
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # credentials are correct, log them in
                response = redirect('index')
                login(request, user)
                return response
            else:
                message = "Username or password is incorrect."
            # direct to login page or diary entry page
        else:
            message = "Something went wrong with the form."
    else:
        # if they're already logged in send them to the home page
        if request.user.is_authenticated:
            print("Checking Login")
            response = redirect('index')
            return response
    # if they're not logged in, load the form
    form = LoginForm()
    context = {
        "message": message,
        "form": form,
    }
    return render(request, 'login.html', context)


def logoutview(request):
    logout(request)
    response = redirect('index')
    return response