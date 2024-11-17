from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def video(request):
    return render(request,'core/video.html')

def chat(request):
    return render(request,'core/chat.html')

def carM(request):
    return render(request,'core/carM.html')

def blog1(request):
    return render(request,'core/blog1.html')

def blog2(request):
    return render(request,'core/blog2.html')

def blog3(request):
    return render(request,'core/blog3.html')