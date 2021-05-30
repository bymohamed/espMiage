from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db import connection

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
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT max("main_temperature"."datetime") as maxDate, "main_classenum"."num", "main_esp"."mac", "main_temperature"."valeur" FROM "main_classenum" JOIN "main_salledeclasse" ON ("main_classenum"."num" = "main_salledeclasse"."numeroDeSalle_id") INNER JOIN "main_esp" ON ("main_salledeclasse"."esp_id" = "main_esp"."mac") INNER JOIN "main_temperature" ON ("main_esp"."mac" = "main_temperature"."who_id") group by "mac"''')
    except:
        print("pas encore intisialisé  ")
    context['valeurs'] = cursor.fetchall()

    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            my_model = form.save()  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively:
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            # my.model.save()
    else:        
        form = SalleForm()
    context['form'] = form

    return render(request,"dashboard.html",context)


@login_required
def tables(request):
    context = {}
    context['temps'] = Temperature.objects.all()
    return render(request, "tables.html", context)


@login_required
def charts(request, oid = None):
    return render(request, "charts.html")