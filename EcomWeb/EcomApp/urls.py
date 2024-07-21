from .import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('product-detail/', views.product_detail, name='product-detail'),
    
]