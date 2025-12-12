from django.urls import path
from .views import RegistrarUserView, OlharUserProfile

urlpatterns = [
    path("registrar/", RegistrarUserView.as_view(), name='registrar'),
    path("me/", OlharUserProfile.as_view(), name='perfil')
]