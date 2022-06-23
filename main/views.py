from django.shortcuts import render
import socket
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def homePageView(request):
    hostname = socket.gethostname()
    return render(request, "hello.html", {'hostname':hostname})
