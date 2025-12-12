from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistroUsuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from .models import User

class RegistrarUserView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = RegistroUsuario(data = request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {"message": "Usuário registrado com sucesso"},
                status = status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OlharUserProfile(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegistroUsuario

    def get_object(self):
        return self.request.user


