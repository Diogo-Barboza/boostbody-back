from django.urls import path
from . import views

urlpatterns = [
    path("registrar/", RegistrarUserView.as_view(), name='registrar')
]