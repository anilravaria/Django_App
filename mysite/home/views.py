from django.shortcuts import render
from django.http import HttpResponse


def home_index(request):
    return HttpResponse("You're at home index")
