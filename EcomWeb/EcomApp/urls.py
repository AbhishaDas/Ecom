from django import views
from django.urls import include, path

urlpatterns = [
    path('',views.signup,name='signup'),
    
]