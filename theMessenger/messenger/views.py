from django.shortcuts import render,redirect
from django.contrib.auth import login as authLogin,authenticate,logout
from django.contrib.auth.models import User
from .models import AuthUser,Friendship
from django.forms import ModelForm
import json
from django.http import JsonResponse
from .util import newUser as userForm,AddFriend,loginDigest
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core import serializers
# Create your views here.


class UserForm(ModelForm):

    class Meta:
        model = AuthUser
        fields = ['username','email','password','first_name','last_name','is_superuser','is_staff','is_active']

class friendForm(ModelForm):
    class Meta:
        model = Friendship
        fields = ['me','friend']
#
#   Sistema de Logon e logoff
#   
def loginHome(request):
    if request.method == "GET" :
        return render(request,'login/register.html')
    elif request.method == "POST":
        if request.POST['username'] != "furtado" :
            bcriptUser = {
                'username':request.POST['username'],
                'password':loginDigest().crypto(password=request.POST['password'])
            }
        else :
            bcriptUser = request.POST

        user = authenticate(username=bcriptUser['username'],password=bcriptUser['password'])

        if user is not None:
            authLogin(request,user)
            return redirect('/home')
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
    return redirect('/')
#
# New user views
# 
@csrf_protect 
def registerView(request):
    user = userForm(data=request.POST).get_values()
    validated = UserForm(user)
    if validated.is_valid :
        User.objects.create_user(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            is_superuser=1,
            is_staff=1,
            is_active=1
        )
        return redirect('/')
    else:
        return redirect('/')
        
@login_required(login_url='')
def home(request):
    try:
        users = Friendship.objects.filter(me=request.user.id,is_accepted=True)
        print('1',len(users))
    except:
        context = {
            "user":request.user,
            "friends":["Adicione um amigo para utilizar o sistema de chat"]
        }
        return(render(request,'messenger/sidebar.html',context))
    print(request.user.id)
    try:
        usuario = AuthUser.objects.get(id=request.user.id)
        friends = Friendship.objects.all().filter(friend=usuario)
        print(friends[0]['me'])
    except:
        solicitacoes = ["Nenhuma solicitação Pendente"]
    user = {
        "user" : request.user,
        "friends": users,
        "solicitation":friends,
    }
    return render(request,'messenger/sidebar.html',user)

@csrf_exempt
def findUsers(request):
    requestValue = json.loads(request.body)
    users = User.objects.filter(username__icontains=requestValue['fieldValue'],id__exact)
    friends = {
        'friends' : users
    }
    return render(request,'messenger/newFriend.html',{'friends' : users})

@csrf_exempt
def addFriend(request):
    requestValue = json.loads(request.body)
    relation = AddFriend({"me":request.user.id,"friend":requestValue["friend_id"]}).getValues()
    friendship = friendForm(relation)
    if friendship.is_valid():
        friendship.save()
        return JsonResponse({"message":"Amigo adicionado"})
    else:
        return JsonResponse({"message":"Erro ao Adicionar Amigo"})
