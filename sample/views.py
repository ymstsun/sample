from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ohanky(request):
    mytext1 = request.GET['myText1']
    mytext2 = request.GET['myText2']

    return render(request, 'ohanky.html',{'mytext1':mytext1,'mytext2':mytext2})

