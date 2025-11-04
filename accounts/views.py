import messages
from django.contrib import auth
from django.shortcuts import render, redirect


def login(request):
    if request.method == "POST":
        return render(request, "accounts/login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('login')
    return redirect('login')


