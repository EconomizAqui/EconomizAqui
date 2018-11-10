from django.urls import path
from django.urls import include
from products import views
urlpatterns = [
    path('', views.list_products ,name='listProducts'),
    path('new', views.create_product ,name='createProduct'),
    path('update/<int:id>/', views.update_product ,name='updateProduct'),
    path('delete/<int:id>/', views.delete_product ,name='deleteProduct'),
]
