from django.urls import path
from . import views

urlpatterns = [
    path('save-type/', views.save_type, name='save'),
    path('create-type/', views.create_type, name='create'),

]