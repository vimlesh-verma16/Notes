from django.urls import path
from basic_app import views

# TEMPLATE TAGGING

app_name = 'basic_app'

#http://127.0.0.1:8000/basic_app/relative/ 

urlpatterns = [
    path('relative/',views.relative ,name='relative'),
    path('other/',views.other,name='other')
]