from django.shortcuts import render, redirect
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
