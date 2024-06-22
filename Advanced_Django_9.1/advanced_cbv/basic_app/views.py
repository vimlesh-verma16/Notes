from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                 DetailView,CreateView,DeleteView,
                                 UpdateView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

# Create your views here.
# def index(request):
#     return render(request,'index.html')

class indexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Text Injection" 
        return context 

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #returns context as  school_list [  models.School lowercase everything after . and adds _list]

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html' 


class SchoolCreateView(CreateView):
    fields = ("name",'principle','location')
    model =models.School
    template_name = 'basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ("name",'principle')
    model =models.School

class SchoolDeleteView(DeleteView):
    model =models.School
    success_url = reverse_lazy('basic_app:list')








    