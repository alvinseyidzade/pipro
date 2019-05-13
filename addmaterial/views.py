from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Data
from home.forms import DataForm
# Create your views here.


@login_required(login_url='/login/')
def addmaterial(request):
    data = Data.objects.all()



    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.ad_soyad = request.POST.get("ad_soyad")
            model_instance.yasadigi_region = request.POST.get("yasadigi_region")
            model_instance.profili = request.POST.get("profili")
            model_instance.elaqenomresi = request.POST.get("elaqenomresi")
            model_instance.problemler = request.POST.get("problemler")

            model_instance.veziyyetsablonu = request.POST.get("status")
            model_instance.seher = request.POST.get("seher")
            model_instance.kend = request.POST.get("kend")
            model_instance.save()
            data = Data.objects.all()

            return render(request, 'index.html', {'data': data})



    else:

        form = DataForm()


    return render(request, "addmaterial.html", {'data': data,'form': form})








def add(request):
    data = Data.objects.all()



    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.ad_soyad = request.POST.get("ad_soyad")
            model_instance.yasadigi_region = request.POST.get("yasadigi_region")
            model_instance.profili = request.POST.get("profili")
            model_instance.elaqenomresi = request.POST.get("elaqenomresi")
            model_instance.problemler = request.POST.get("problemler")

            model_instance.veziyyetsablonu = request.POST.get("status")
            model_instance.seher = request.POST.get("seher")
            model_instance.kend = request.POST.get("kend")
            model_instance.save()
            data = Data.objects.all()

            return render(request, 'baza.html', {'data': data})



    else:

        form = DataForm()


    return render(request, "add.html", {'data': data,'form': form})
