from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def userlog(request):
    return render(request,'userlog.html')

# Create your views here.
