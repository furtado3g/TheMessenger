from django.shortcuts import render

# Create your views here.
def loginHome(request):
    if request.method == "GET" :
        return render(request,'login/login.html')