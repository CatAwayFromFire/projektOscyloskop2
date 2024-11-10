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
    # Extract the command from the form submission
    command = request.POST.get('command')
    if command:
        print(f"Received command: {command}")
        send_command(command)
        return HttpResponseRedirect("/")  # Redirect to the homepage after sending the command
    else:
        return HttpResponse("No command provided", status=400)
