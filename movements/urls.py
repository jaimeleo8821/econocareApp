from django.urls import path
from . import views
from movements.views import(
    MovementHTMxTableView
)

urlpatterns = [
    path('create-type/', views.create_type, name='create_type'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-pay-method/', views.create_payMethod, name='create_pay_method'),
    path('create-movement/', views.create_movement, name='create_movement'),
    path('create-origin/', views.create_origin, name='create_origin'),
    path('category/<str:slug>', views.category, name='category'),
    path('type/<str:slug>', views.type, name='type'),
    path('pay-method/<str:slug>', views.pay_method, name='pay_method'),
    path('movements-table', MovementHTMxTableView.as_view(), name='movement_table')

]