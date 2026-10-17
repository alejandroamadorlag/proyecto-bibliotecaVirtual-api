from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from proyecto_bibliotecaVirtual_api.serializers import *
from proyecto_bibliotecaVirtual_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json


class VersionView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):

        return Response({"version":"1.0.0"})


class DashboardContadores(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        data = {
            "total_libros":               Libros.objects.exclude(eliminado=1).count(),
            "prestamos_proceso":          Prestamos.objects.filter(is_active=1).count(),
            "clientes_registrados":       Clientes.objects.filter(user__is_active=1).count(),
            "bibliotecarios_registrados": Bibliotecarios.objects.filter(user__is_active=1).count(),
            "generos_registrados":        Generos.objects.filter(is_active=1).count(),
            "autores_registrados":        Autores.objects.filter(is_active=1).count(),
        }
        return Response(data, 200)

# DashboardContadores con impresion de contadores en consola
"""
class DashboardContadores(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        total_libros               = Libros.objects.filter(is_active=1).count()
        prestamos_proceso          = Prestamos.objects.filter(is_active=1).count()
        clientes_registrados       = Clientes.objects.filter(user__is_active=1).count()
        bibliotecarios_registrados = Bibliotecarios.objects.filter(user__is_active=1).count()
        generos_registrados        = Generos.objects.filter(is_active=1).count()
        autores_registrados        = Autores.objects.filter(is_active=1).count()

        print("=== CONTADORES ===")
        print("Libros         -> total:", Libros.objects.count(), "| is_active=1:", total_libros)
        print("is_active reales:", list(Libros.objects.values_list("id_libro", "is_active"))[:10])
        print("Prestamos      -> total:", Prestamos.objects.count(), "| en proceso:", prestamos_proceso)
        print("Clientes       -> total:", Clientes.objects.count(), "| activos:", clientes_registrados)
        print("Bibliotecarios -> total:", Bibliotecarios.objects.count(), "| activos:", bibliotecarios_registrados)
        print("Generos        ->", generos_registrados, "| Autores ->", autores_registrados)

        data = {
            "total_libros": total_libros,
            "prestamos_proceso": prestamos_proceso,
            "clientes_registrados": clientes_registrados,
            "bibliotecarios_registrados": bibliotecarios_registrados,
            "generos_registrados": generos_registrados,
           "autores_registrados": autores_registrados,
        }
        return Response(data, 200)
"""