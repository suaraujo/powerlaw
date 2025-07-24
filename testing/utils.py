import os
from numpy import genfromtxt

def load_reference_data(name, log_transform=False, scale=1.0):
    """
    Carga el archivo de datos de la carpeta `reference_data/`archivo.

    Parámetros
    ----------
    name : str
        Nombre del archivo (por ejemplo, 'words.txt').
    log_transform : bool
        Si es True, se aplica 10**data (útil para datos en escala logarítmica como 'quakes.txt').
    scale : float
        Factor por el cual dividir los datos después de la carga.

    Retorna
    -------
    ndarray
        Arreglo de datos cargado.
    """
    here = os.path.dirname(__file__)
    path = os.path.join(here, 'reference_data', name)
    data = genfromtxt(path)
    if log_transform:
        data = 10 ** data
    return data / scale