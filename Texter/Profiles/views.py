from django.shortcuts import render
from .forms import Profile_Login
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def Profile_Page(request, username):
    return render(request, 'Profiles/Profile_Page.html', {'username':request.user.username})

def Edit_Profile_Page(request, username):
    return render(request, 'Profiles/Edit_Profile_Page.html', {'username':request.user.username})

def Login(request):
    if request.method == "POST":
        form = Profile_Login(request.POST)
        Username = request.POST['Username']
        Password = request.POST['Password']
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return render(request, 'Profiles/Success.html', {'username':request.user.username})
        else:
            return render(request, 'Profiles/Fail.html', {})
    else:
        form = Profile_Login()
    return render(request, 'Profiles/Login.html', {'form':form})

def Logout(request):
    logout(request)
    return render(request, 'Home/index.html', {'username':request.user.username})

def Register(request):
    return render(request, 'Profiles/Register', {'username':request.user.username})
