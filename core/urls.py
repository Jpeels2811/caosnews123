from django.urls import path
from .views import main, paginaregister


urlpatterns = [
    path('', main,name="main"),
    path('PaginaRegister/',paginaregister,name="paginaregister"),
    
    ]
