from django.shortcuts import render,redirect
from django.contrib.auth import login as authLogin,authenticate,logout
# Create your views here.

#
#   Sistema de Logon e logoff
#   
def loginHome(request):
    if request.method == "GET" :
        return render(request,'login/login.html')
    elif request.method == "POST":
        user = authenticate(username=request.POST['login'],password=request.POST['senha'])
        if user is not None :
            authLogin(request,user)
            logado = True
            context = {
                "logado" : logado
            }
            return render(request,'login/login.html',context)
        else:
            logado  = True
            message = "Usuario ou Senha incorretos"
            context = {
                "logado" : logado,
                "message" : message
            }
            return render(request,'login/login.html',context)

def logoutView (request):
    logout(request)
    redirect('')
#
# New user views
# 
