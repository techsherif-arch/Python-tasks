from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
# Create your views here.

def homepage(request):
    return render(request,'homepage.html')
def aboutpage(request):
    return render(request,'aboutpage.html')
def loginform(request):
    return render(request,'loginform.html')
def logincheck(request):
    uname=request.POST.get('username')
    upass=request.POST.get('userpassword')
    if uname=='admin' and upass=='pass@123':
        # return render(request,'adminpage.html')
        return render(request,'adminpage.html')
    else:
        return render(request,'loginform.html')