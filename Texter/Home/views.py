from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'Home/index.html', {'username':request.user.username})