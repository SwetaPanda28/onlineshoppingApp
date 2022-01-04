from django.http.response import HttpResponse
from django.shortcuts import render   
from django.http import HttpRequest



def index(request :HttpRequest):
    return HttpResponse("hello")

