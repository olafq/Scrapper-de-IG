from selenium import webdriver
from langdetect import detect
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import os
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd # clave para el prosesamiento de informacion de manera ordeanada 
from datetime import datetime as dt #para manejar fechas
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager # con esta libreria solucionamos el tema de compatibilidad entre chromedriver y google chrome

def esperar_elemento(driver, by, selector, tiempo_espera=200):
    return WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located((by, selector))
    )

def esperar_elementos(driver, by, selector, tiempo_espera=60):
    return WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_all_elements_located((by, selector))
    )

def traer_usuarios_a_buscar(ruta):
    # Abre el archivo de texto en modo lectura
    with open(ruta, "r") as archivo:
        usuariosABuscar = []
        # Itera sobre cada línea del archivo
        for linea in archivo:
            # Elimina espacios en blanco al principio y al final de la línea
            usuario = linea.strip()
            # Agrega el usuario a la lista
            usuariosABuscar.append(usuario)
    return usuariosABuscar
# funcion que Cierra el navegador
def cerrrarNavegador(driver):
    driver.quit()

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

def ingresar_us_cont(driver,us,pas):
    # Espera hasta que el elemento esté presente en la página
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    # Ingresa el nombre de usuario en el campo usuario de la web
    username_input.send_keys(us)
    # Espera hasta que el elemento esté presente en la página
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    # Ingresa la contraseña en el campo contraseña de la web
    username_input.send_keys(pas)

def inicializarChrome():
    ruta = os.getcwd()
    driver_path = os.path.join(ruta, 'chromedriver.exe')
    service = ChromeService(executable_path=driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Opcional, maximiza la ventana del navegador al iniciar
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
    
    
def generarDF(data,nombreArchivo,nombre_carpeta):
    df = pd.DataFrame(data)
    ruta_actual = os.getcwd()
    ruta_a_crear_el_excel = os.path.join(ruta_actual, nombre_carpeta)
    excel_a_crear = os.path.join(ruta_a_crear_el_excel,nombreArchivo)
    df.to_excel( excel_a_crear , index=False)