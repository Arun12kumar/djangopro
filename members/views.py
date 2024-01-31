from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import data
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        datafirst = request.POST.get('firstname')
        datalast = request.POST.get('lastname')
        dataemail = request.POST.get('email')
        dataphone = request.POST.get('phone')
        datapassword = request.POST.get('password')
        datagender = request.POST.get('gender')
        data(firstname=datafirst,lastname=datalast,email=dataemail,phone=dataphone,password=datapassword,gender=datagender).save()
    return render(request,"register.html")    

def login(request):
    return render(request,"login.html")

def table(request):
    cr = data.objects.all()
    return render(request,"table.html",{'cr':cr}) 

def detailed(request,pk):
    cr = data.objects.get(id=pk)   
    return render(request,"detail.html",{'cm':cr}) 

def deleted(request,pk):
    cr = data.objects.get(id=pk)
    cr.delete()   
    return redirect ("table")

def edited(request,pk):
    cr = data.objects.get(id=pk)
    if request.method == "POST":
        cr.firstname = request.POST.get('firstname')
        cr.lastname = request.POST.get('lastname')
        cr.email = request.POST.get('email')
        cr.phone = request.POST.get('phone')
        cr.password = request.POST.get('password')
        cr.gender = request.POST.get('gender')
        cr.save()

        return redirect("table")
    return render(request, "edit.html", {'cr': cr})


def userlog(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        password = request.POST.get('password')
        cr = data.objects.filter(firstname=firstname,password=password)
        if cr:
            user_detail = data.objects.get(firstname=firstname,password=password)
            id = user_detail.id
            firstname = user_detail.firstname

            request.session['id']=id
            request.session['firstname']=firstname

            return redirect ('home')
        
        else:
            return render(request,'login.html',
            messages.error(request,'incorrect username or password'))
        
    else:
        return render(request,'table.html')    
    

def home(request):
    return render(request,'home.html')  

def newlogin(request):
    return render(request,"newlogin.html") 


def alog(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
            
        else:
            return redirect(request,'newlogin')
            
    else:
        return render(request,'table.html')

