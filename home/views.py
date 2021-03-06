from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Data
from .forms import DataForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    data = Data.objects.all()


    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.ad_soyad = request.POST.get("input_quality")
            model_instance.unit = request.POST.get("unit")
            model_instance.date = request.POST.get("date")
            model_instance.comment = request.POST.get("comment")
            model_instance.user = request.user
            model_instance.save()
            data = Data.objects.all()

            return render(request, 'baza.html', {'data': data})



    else:

        form = DataForm()
    return render(request, "baza.html", {'data': data})






@login_required(login_url='/login/')
def dashboard2(request):
    data = Data.objects.all()


    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.ad_soyad = request.POST.get("input_quality")
            model_instance.unit = request.POST.get("unit")
            model_instance.date = request.POST.get("date")
            model_instance.comment = request.POST.get("comment")
            model_instance.user = request.user
            model_instance.save()
            data = Data.objects.all()

            return render(request, 'index.html', {'data': data})



    else:

        form = DataForm()
    return render(request, "index.html", {'data': data})




@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user')
        else:
            return redirect('user')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'changepassword.html', args)

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required(login_url='/login/')
def post_update(request, id):
    post = get_object_or_404(Data, id=id)
    form = DataForm(request.POST or None, request.FILES, instance=post)
    data = Data.objects.all()
    if request.method == 'POST' and request.FILES['image']:

        if form.is_valid():
            handle_uploaded_file(request.FILES['image'])
            model_instance = form.save(commit=False)
            model_instance.ad_soyad = request.POST.get("ad_soyad")
            model_instance.yasadigi_region = request.POST.get("yasadigi_region")
            model_instance.profili = request.POST.get("profili")
            model_instance.elaqenomresi = request.POST.get("elaqenomresi")
            model_instance.problemler = request.POST.get("problemler")

            model_instance.veziyyetsablonu = request.POST.get("status")
            model_instance.seher = request.POST.get("seher")
            model_instance.kend = request.POST.get("kend")
            image = request.FILES.get('image', False)
            model_instance.save()
            return render(request, 'baza.html', {'data': data})

    return render(request, "update.html", {'form': form, 'post':post})
