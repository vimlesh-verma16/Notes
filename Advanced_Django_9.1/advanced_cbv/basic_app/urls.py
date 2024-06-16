from django.contrib import admin
from django.urls import path,include
from basic_app import views,urls

app_name = 'basic_app'
urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),

]