from django.urls import path
from . import views

urlpatterns = [
    path('checkuser/', views.checkuser, name="checkuser"),
    path('visualize/', views.visualize, name="visualize"),
    path('test_send/', views.test_send, name="test_send"),
    path('test_visualize/', views.test_visualize, name="test_visualize"),
    path('test/', views.visualize, name="test"),
]

