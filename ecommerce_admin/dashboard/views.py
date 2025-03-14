from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

# forgot password
"""
def forgot_password(request):
    return render(request, "forgot_password.html") 
"""
