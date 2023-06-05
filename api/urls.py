from django.urls import path

from .views import EnamelListCreateAPIView

urlpatterns = [
    path('', EnamelListCreateAPIView.as_view()),
]
