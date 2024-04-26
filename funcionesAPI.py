import requests
import os
import pandas as pd
def contar_archivos_txt(ruta_carpeta):
    # Obtiene la lista de archivos en la carpeta especificada
    archivos = os.listdir(ruta_carpeta)
    # Inicializa un contador para archivos .txt
    contador = 0

    # Recorre la lista de archivos y cuenta los que tienen extensión .txt
    for archivo in archivos:
        if archivo.endswith(".txt"):
            contador += 1

    return contador

def generarDF(data,nombreArchivo,nombre_carpeta):
    df = pd.DataFrame(data)
    ruta_actual = os.getcwd()
    ruta_a_crear_el_excel = os.path.join(ruta_actual, nombre_carpeta)
    excel_a_crear = os.path.join(ruta_a_crear_el_excel,nombreArchivo)
    df.to_excel( excel_a_crear , index=False)