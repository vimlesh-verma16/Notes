from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html')

def forms_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print("Validation Succesfull")
            print("Name"+ form.cleaned_data["name"])
            print("Detail"+ form.cleaned_data["detail"])
            print("EMAIL"+ form.cleaned_data["email"])
            print("Text"+ form.cleaned_data["text"])
    return render(request,"forms.html",{'form':form})
