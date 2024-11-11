from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from connection.connect import send_command, send_query
from connection.commands import commands,queries
def index(request):
    return render(request, 'website/index.html',{"commands":commands,"queries":queries})

def querybutton(request):
    query = request.POST.get('query')
    if query:
        data = send_query(query)
        return JsonResponse({"result": data})  # Return JSON response
    else:
        return JsonResponse({"error": "No query provided"}, status=400)

def commandbutton(request):
    command = request.POST.get('command')
    if command:
        send_command(command)
        return JsonResponse({"status": "Command sent successfully"})
    else:
        return JsonResponse({"error": "No command provided"}, status=400)


