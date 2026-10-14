import datetime
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from proyecto_bibliotecaVirtual_api.file_storage.file_system_storage import FileSystemStorage

class FileStorageFactory:

    @staticmethod
    def create():
        #TODO: Aqui se puede elegir que tipo de storage usar
        return FileSystemStorage()