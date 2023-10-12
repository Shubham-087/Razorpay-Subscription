from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/<str:id>', views.payment, name='payment'),
    path('success', views.success, name='success'),
]
