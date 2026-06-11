from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove'),

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),

    path('increase/<int:id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease'),
    path('login/', views.user_login, name='login'),
]