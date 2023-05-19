from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_list/', views.index, name='sample_list'),
    path('add_sample/', views.index, name='add_sample'),
    path('contacts/', views.index, name='contacts'),
    path('sample/<str:pk>', views.index, name='contacts'),
]