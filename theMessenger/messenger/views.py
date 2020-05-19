from django.shortcuts import render,redirect
from django.contrib.auth import login as authLogin,authenticate,logout
from .models import AuthUser
from django.forms import ModelForm
import json
from .util import newUser as userForm
# Create your views here.


class UserForm(ModelForm):

    class Meta:
        model = AuthUser
        fields = ['username','email','password','first_name','last_name','is_superuser','is_staff','is_active']

#
#   Sistema de Logon e logoff
#   
def loginHome(request):
    if request.method == "GET" :
        return render(request,'login/register.html')
    elif request.method == "POST":
        user = authenticate(username=request.POST['login'],password=request.POST['senha'])
        if user is not None :
            authLogin(request,user)
            logado = True
            context = {
                "logado" : logado
            }
            return render(request,'login/register.html',context)
        else:
            logado  = True
            message = "Usuario ou Senha incorretos"
            context = {
                "logado" : logado,
                "message" : message
            }
            return render(request,'login/register.html',context)

def logoutView (request):
    logout(request)
    return render(request,'login/register.html')
#
# New user views
# 
def registerView(request):
    user = userForm(data=request.POST).get_values()
    convertedUser = UserForm(user)
    if convertedUser.is_valid():
        convertedUser.save()
        return redirect('/')
    else:
        logado = False,
        message = "Erro ao Tentar se Registrar Tente novamente mais tarde"
        context = {
            "logado" : logado,
            "message" : message
        }
        return render(request,'login/register.html',context)