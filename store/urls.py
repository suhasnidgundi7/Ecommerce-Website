from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about-us/', views.about, name="about-us"),
    path('contact-us/', views.contact, name="contact-us"),

    path('update_item/', views.updateItem, name="update_item"),

]