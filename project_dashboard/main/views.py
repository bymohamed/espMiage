from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def viewlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(dashboard)

    return render(request, "login.html")

@login_required
def dashboard(request):
    # alltemps = Temperature.objects.all()
    # text = ""
    # for temp in alltemps:
    #     text += "|"+temp.datetime.strftime("%d-%b-%Y (%H:%M:%S.%f)")+"|"+str(temp.valeur)+"|"+str(temp.who)+"<br>"
    context = {}
    context['temps'] = Temperature.objects.all()

    return render(request,"dashboard.html",context)

def datarecup(request):
    temperature = request.GET.get("temp")
    print(temperature)
    machine = request.GET.get("machine")
    print(machine)
    new = Temperature(valeur=float(temperature), idmachine=int(machine))
    new.save()
    print(Temperature.objects.all())
    return HttpResponse("waiting for data")

def tables(request):
    context = {}
    context['temps'] = Temperature.objects.all()
    return render(request, "tables.html", context)