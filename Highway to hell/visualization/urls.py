from django.urls import path
from . import views

urlpatterns = [
    path('underdev/', views.underDev, name="vis_af_dev"),
    path('test3/', views.test3, name="vis_test3"),
    path('test_send/', views.test_send, name="test_send"),
]
