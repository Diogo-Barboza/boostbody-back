from django.urls import path
from .views import RegistrarUserView

urlpatterns = [
    path("registrar/", RegistrarUserView.as_view(), name='registrar')
]