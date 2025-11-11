import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from pyexpat.errors import messages

def submit_login(request):
    if request.method != "POST":
        return render(request, "accounts/submit_login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('listar_contato')
    return redirect('submit_login')


