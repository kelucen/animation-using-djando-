
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('animacao1', views.animacao1),
    path('animacao2', views.animacao2),
    path('deslizamento', views.landslide),
    path('deslizamentoManaus', views.landslideManaus),

]
