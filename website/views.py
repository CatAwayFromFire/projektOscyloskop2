from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from connection.connect import send_command, send_query
from connection.commands import commands,queries
def index(request):
    return render(request, 'website/index.html',{"commands":commands,"queries":queries})

def button(request):

    message = request.POST.get('query')
    type_ = request.POST.get('type')
    print(message,type_)
    if message:
        if type_ == "query":

            data = send_query(message)
            print(data)
        if type_ == "command":

            send_command(message)
    return HttpResponseRedirect('/')


