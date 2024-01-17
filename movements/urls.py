from django.urls import path
from . import views

urlpatterns = [
    path('create-type/', views.create_type, name='create_type'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-pay-method/', views.create_payMethod, name='create_pay_method'),

]