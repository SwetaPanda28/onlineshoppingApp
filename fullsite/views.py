from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.urls.base import reverse
import razorpay
from razorpay import client
from . import models,forms
from math import ceil
from onlineshoppingApp import settings
from django.views.decorators.csrf import csrf_exempt

client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

def home(request :HttpRequest):
    userid=request.COOKIES.get('id',False)
    prods=models.Product.objects.all()
    n= len(prods)
    nslides = n//4 + ceil ((n/4)-(n//4))
    prodList=[]
    start=0
    for i in range(nslides):
        prodList.append(prods[start:start+4])
        start+=4

    cart=models.Cart.objects.get(user_id=userid)
    params={'prodlist':prodList,'number':len(cart.products.values())}
    return render(request,'fullsite/home.html',params)

def gateway(request : HttpRequest):
    return render(request,'fullsite/gateway.html')
    


def productview(request :HttpRequest): #ek product ka description
    pid=request.GET.get("pid",False)
    if(not pid):
        return HttpResponse('object not found')
    pro=models.Product.objects.get(id=pid)  
    userid=request.COOKIES.get('id',False)
    cart= models.Cart.objects.get(user_id=userid)
    params={'product':pro, 'number':len(cart.products.values())}
    return render(request,'fullsite/productview.html',params)


def cart(request :HttpRequest):                         # user ke sath one to one reln and product ke sath many to one
    userid=request.COOKIES.get('id',False)
    cart=models.Cart.objects.get(user_id=userid)
    if(request.method=='POST'):
        product=request.POST.get('pid',False)
        action=request.POST.get('act','add')#act value hai =remove  agar remove milta hai if 1st wala condition kam karega otherwisw post request kuch bi ajata hai toh phir wah get karega
        cart : models.Cart
        if(action=="remove"):
            cart.products.remove(product)
        else:
            cart.products.add(product)
        cart.save()
    params={'products':cart.products.values(),
            'number':len(cart.products.values())}

    return render(request,'fullsite/cart.html',params)


def about(request :HttpRequest):
    return render(request,'fullsite/about.html')

def order(request: HttpRequest):
    id=request.COOKIES.get('id',None)
    if(id):
        pass

def addAddress(request :HttpRequest):
    if(request.method=="POST"):
        form=forms.AddressForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('payment')
        else:
            print(form.errors)
    form=forms.AddressForm()
    params={'form':form}
    return render(request,'fullsite/order2.html',params)

def contact(request :HttpRequest):
    return render(request,'this is conct')


def trackeringsatus(request :HttpRequest):
    return render(request,'this is conct')

def search(request :HttpRequest):
    return render(request,'this is conct')


def payment(request :HttpRequest):
    import razorpay
    import time

    global client
    userid=request.COOKIES.get('id',False)
    cart=models.Cart.objects.get(user_id=userid)#user= means hum jahape search karrehe hai
    price=0
    for product in cart.products.all():
        price+=product.price
    #here we are add all the products
    #rec=str(time.localtime())[:20]
    price*=100
    data={                                       
        'amount':price,
        'currency': 'INR',
        #'receipt' : rec
    }
    orderObj=client.order.create(data=data)   #razpay ko data bhejrehe hai
    id=orderObj.get('id','')

    params={           #data send to front end
        'orderId' : id,
        'mkey' : settings.RAZORPAY_KEY_ID,
        'amount' : int(price),
        #'recept' : rec,
        'currency':  'INR',
        'callbackUrl': request.build_absolute_uri(reverse('payment_complete',kwargs={'userPk':cart.user.pk}) ),
    }

    return render(request,'fullsite/paymentR.html',params)

@csrf_exempt
def payment_complete(request,userPk):
    
    razorpay_payment_id=request.POST.get("razorpay_payment_id",False)
    razorpay_order_id=request.POST.get("razorpay_order_id",False)
    razorpay_signature=request.POST.get("razorpay_signature",False)
    print(razorpay_order_id,razorpay_payment_id,razorpay_signature)

    global client
    try:
        client.utility.verify_payment_signature({
            "razorpay_payment_id" : razorpay_payment_id,
            "razorpay_order_id" : razorpay_order_id,
            "razorpay_signature" : razorpay_signature
        })
        
        return render(request,'fullsite/gateway.html')
    except Exception:
        return HttpResponse("Your payment failed")
