from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HotDish'),
    path('Brubakers/', views.brubakers, name='Brubakers'),
    path('V1/', views.V1, name='V1'),
    path('REV/', views.REV, name='REV'),
    path('CMH/', views.CMH, name='CMH'),
    path('SCH/', views.SCH, name='SCH'),

]