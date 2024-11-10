from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from connection.connect import send_command,send_query
# Create your views here.
def index(request):
    return render(request, 'website/index.html')
def querybutton(request,text):
    print(text)
    data = send_query(text)
    print("to co yszslo ", data)
    return HttpResponse(data)
def commandbutton(request,text):
    print(text)
    send_command(text)

    return HttpResponseRedirect("/")
