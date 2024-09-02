from django.urls import path 
from . import views

urlpatterns = [
    path("",views.landing,name='book'),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("about/",views.about,name='about'),
    
    
]