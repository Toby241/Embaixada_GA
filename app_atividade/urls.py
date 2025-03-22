from django.urls import path
from .views import servicos


# urls.py
from django.urls import path
from .views import dashboard_view

urlpatterns = [

    path('dashboard/', dashboard_view, name='ir-para-dashboard'),
    
    path('', servicos, name='servicos'),
]
