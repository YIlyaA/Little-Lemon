from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menuview.as_view()),
    path('booking/', views.bookingview.as_view()),
]