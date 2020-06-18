from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    form =UserCreationForm()
    print("-----")
    print(request.method)
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        print(form.is_valid)
        if form.is_valid():
            print("save")
            form.save()
    context={"form" :form}
    return render(request,'register.html',context)
