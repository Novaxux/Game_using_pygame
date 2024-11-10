import os, sys

def resource_path(relative_path):
    """ Devuelve la ruta absoluta de un archivo de recursos, tomando en cuenta si está empaquetado con PyInstaller """
    try:
        # Cuando se ejecuta en el ejecutable empaquetado por PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Cuando se ejecuta en el entorno de desarrollo
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
