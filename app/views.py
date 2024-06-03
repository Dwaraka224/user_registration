from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse



def registration(request):
    EUFO=UserForm()#Empty user from object
    EPFO=ProfileForm()#Empty profile form object
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMPFDO.is_valid and NMUFDO.is_valid:
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('Registration successfully completed')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'registration.html',d)