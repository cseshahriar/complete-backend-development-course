from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

def hello(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})