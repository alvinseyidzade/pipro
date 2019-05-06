from django.shortcuts import render
from .models import Data
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    data = Data.objects.all()


#    if request.method == 'POST':
#        form = OutMaterialForm(request.POST)
    #    if form.is_valid():

        #    model_instance = form.save(commit=False)
        #    model_instance.input_quality = request.POST.get("input_quality")
        #    model_instance.unit = request.POST.get("unit")
        #    model_instance.date = request.POST.get("date")
        #    model_instance.comment = request.POST.get("comment")
        #    model_instance.received = request.POST.get("received")
        #    model_instance.id_number = request.POST.get("idnumber")
        #    model_instance.used_type = request.POST.get("usedtype")
        #    model_instance.user = request.user
        #    model_instance.save()
        #    outmaterials = OutMaterial.objects.all()

        #    return render(request, 'index.html', {'data': data})



#    else:

    #    form = OutMaterialForm()


    return render(request, "index.html",{'data': data})
