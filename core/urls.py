from django.urls import path

from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('add_contato/',views.add_contato,
         name='add_contato'),
    path('listar_contato/',views.listar_contato,name='listar_contato')
]