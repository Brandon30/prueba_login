from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
def pag_login(request):
              return render(request, 'pag_login.html')

def pag2(request):
    return render(request, 'pag2.html')