from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistroUsuario

class RegistrarUserView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = RegistroUsuario(data = request.data)

        if serializer.is_valid():
            user = serializer.save()

            

