from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from connection.connect import send_command, send_query
from connection.commands import commands,queries
def index(request):
    return render(request, 'website/index.html', {"commands":commands, "queries":queries})



def button(request):
    if request.method == "POST":
        message = request.POST.get('query')
        type_ = request.POST.get('type')

        if message:
            if type_ == "query":
                # Handle query (AJAX), return JSON
                data = send_query(message)
                return JsonResponse({'data': data})

            elif type_ == "command":
                # Handle command (no page refresh, no JSON response)
                send_command(message)
                return JsonResponse({'data': 'Command executed successfully'})

    return redirect('/')  # Redirect to homepage or another page after POST
