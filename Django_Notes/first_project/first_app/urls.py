from django.urls import path
from first_app import views
from django.conf.urls.static import static 
urlpatterns = [ 
    path('',views.index,name='index')

]