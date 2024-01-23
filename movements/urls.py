from django.urls import path
from . import views

urlpatterns = [
    path('create-type/', views.create_type, name='create_type'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-pay-method/', views.create_payMethod, name='create_pay_method'),
    path('create-movement/', views.create_movement, name='create_movement'),
    path('create-origin/', views.create_origin, name='create_origin'),
    path('category/<str:slug>', views.category, name='category'),
    path('type/<str:slug>', views.type, name='type'),
    path('origin/<str:slug>', views.origin, name='origin'),
    path('pay-method/<str:slug>', views.pay_method, name='pay_method'),
    path('movements/', views.list_movements, name="list_movements")

]