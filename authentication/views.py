from django.db.models import query
from django.shortcuts import redirect, render
from . import models   
from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt

def signIn(request :HttpRequest): 
    if(request.method=='POST'):
        email=request.POST.get('email',False)
        fname=request.POST.get('fname',False)
        lname=request.POST.get('lname',False)
        password=request.POST.get('pwd',False)
        phno=request.POST.get('phone',False)
        gender=request.POST.get('gender',"female")
        print(email)
        print(fname)
        print(lname)
        print(password)
        print(phno)
        print("female")
        if(len(models.User.objects.filter(emailAddress=email))==0):
            user=models.User(firstname=fname,lastname=lname,password=password,phonenumber=phno,gender=gender,emailAddress=email)
            user.save()
            resp=redirect('index')
            resp.set_cookie('id',user.id)
            return resp

    return render(request,'authentication/signin.html')
    
@csrf_exempt
def login(request :HttpRequest):
    if(request.method=='POST'):
        email=request.POST.get('email',False)
        password=request.POST.get('pass',False)
        query=models.User.objects.filter(emailAddress=email,password=password)
        print(email,password)
        if(len(query)>0):
            user=query[0]
            resp=redirect('index')
            resp.set_cookie('id',user.id)
            return resp

    return render(request,'authentication/login.html')


def logout(request :HttpRequest):
    
    resp=redirect('login')
    resp.delete_cookie("id")
    return resp


# Create your views here.
