
from blog.models import Blogg, Contact
from django.contrib import messages
from django.shortcuts import HttpResponse, render


def index(request):
    return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the polls index.")
def about(request):
    return HttpResponse("ABOUT PAGE")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
        messages.success(request, "success")
    
    return render(request, 'contact.html')

def blogg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        blogg = Blogg(name=name, desc=desc)
        blogg.save()
        messages.success(request, "success")
    return render(request,'blogg.html')


def blogpost(request):
    return render(request,'blogpost.html')
    return HttpResponse("Resources idhar aaenge")
def search(request):
    return render(request,'search.html')