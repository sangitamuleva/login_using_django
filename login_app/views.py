from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:

        form =CreateUserForms()

        if request.method=='POST':
            form=CreateUserForms(request.POST)

            if form.is_valid():
                # save data in database
                form.save()
                # get user
                user=form.cleaned_data.get('username')
                messages.success(request,"Registration is completed for user "+user)
                return redirect('login')
        context={"form" :form}
        return render(request,'register.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else :
                messages.info(request,'Username Or Password Is Incorrect')


        context={}
        return  render(request,'login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context={}
    return render(request, 'home.html', context)
