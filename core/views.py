from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# def index(request):
#     return redirect("/agenda/")

def login_user(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("/")

def submit_login(reqeust):
    if reqeust.POST:
        username = reqeust.POST.get("username")
        password = reqeust.POST.get("password")
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(reqeust, usuario)
            return redirect("/")
        else:
            messages.error(reqeust, "Usuario ou senha invalidos!")
    return redirect("/")

@login_required(login_url="/login/")
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {"eventos": evento}
    return render(request, "agendas.html", dados)