from django.urls import path

from pages import views


urlpatterns = [
    path('products/', views.contact_us, name='products'),
    path('offers/', views.about_us, name='offers'),
    path('', views.home, name='home'),
]