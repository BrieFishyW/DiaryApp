from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def index(request):
    # if logged in, direct to overview page, otherwise go to login page
    if not request.user.is_authenticated:
        response = redirect('login')
    else:
        response = redirect('diary')
    return response
