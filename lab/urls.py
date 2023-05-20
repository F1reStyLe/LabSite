from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_list/', views.sample_list, name='sample_list'),
    path('add_sample/', views.add_sample, name='add_sample'),
    path('contacts/', views.contacts, name='contacts'),
    path('sample/<str:pk>', views.sample, name='sample'),
]