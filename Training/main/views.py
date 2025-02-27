from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

# Introduction
def introduction(request:HttpRequest):

  return render(request, "main/introduction.html")


def css_introduction(request:HttpRequest):
  return render(request,"main/css_introduction.html")