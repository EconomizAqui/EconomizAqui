from django.urls import path

from markets import views

urlpatterns = [
    path('', views.market_list, name='market_list'),
    path('view/<int:pk>', views.market_view, name='market_view'),
    path('new', views.market_create, name='market_new'),
    path('edit/<int:pk>', views.market_update, name='market_edit'),
    path('delete/<int:pk>', views.market_delete, name='market_delete'),
]