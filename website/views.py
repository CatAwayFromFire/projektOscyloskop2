from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from connection.connect import send_command, send_query, gensetup
from connection.commands import commands,queries
def index(request):
    return render(request, 'website/index.html', {"commands":commands, "queries":queries})

def lvl(request,number):
    poziom = [{"freq":2000,"volt":5,"func":"sin"},]
    freq = poziom[number-1]["freq"]
    volt = poziom[number-1]["volt"]
    func = poziom[number-1]["func"]
    send_command("*RST")
    gensetup(freq,volt,func)
    return render(request, f'website/lvl{number}.html',poziom[number-1])

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
