import sys
import os

def resource_path(relative_path):
    #función para obtener el directorio temporal que crea el ejecutable y agregarselo a nuestra ruta relativa.
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)