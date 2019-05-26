from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm



def index(request):
    if request.method == 'POST': #if the form is submitted
        form = UserCreationForm(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            print(data.value())

            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = UserCreationForm()

    return render(request,'login/login_page.html',{'form':form})
