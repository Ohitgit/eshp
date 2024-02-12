from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username, email=email ,password=password,)
        user.save()
        messages.success(request, 'Singup  successful')
    return render(request,"register.html")


#login
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Logged in Successfully")
            return redirect('/')
        else:
            messages.info(request, "Cradiantal doesnot match")
            return HttpResponseRedirect(request.path_info)
    return render(request,"login/login.html")

def dashboard(request):
    return HttpResponse("dashboard")