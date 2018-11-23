from django.urls import path
from django.urls import include
from products import views
urlpatterns = [
    path('', views.list_products ,name='listProducts'),
    path('new', views.create_product ,name='createProduct'),
    path('view/<int:id>/', views.view ,name='viewProduct'),
    path('update/<int:id>/', views.update_product ,name='updateProduct'),
    path('delete/<int:id>/', views.delete_product ,name='deleteProduct'),
    path('addPrice/<int:id>/', views.new_price ,name='newPrice'),
    path('shopping_list/', views.shopping_list ,name='shopping_list'),
]
