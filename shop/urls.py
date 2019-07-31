from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail_1/', views.detail_1, name='detail_1'),
    path('detail_2/', views.detail_2, name='detail_2'),
    path('detail_3/', views.detail_3, name='detail_3'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('mypage/', views.mypage, name='mypage'),
    path('order/new/', views.order_new, name='order_new'),
    path('order/complete', views.order_save, name='order_save'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/edit/', views.order_edit, name='order_edit'),
    path('order/<int:order_id>/delete/', views.order_delete, name='order_delete'),  
]
