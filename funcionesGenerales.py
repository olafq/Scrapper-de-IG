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
import requests
import json

def getCreds() :
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'EAAJIp9alpSQBO26ZB1txhBKxf6WKvZCSKD7YhLGrnZCueLA5LagrQIMyykNePSFdZCWJBYVaeuZCK31CkJoz0k19cNCbIzjco0BsNBARRIKwyvD5nkW0Vg4hjqQtwhNUArq2JSilKAzJT0xNQJJgoCaEL05eYHPMZBNEkqNJrCJ3oiELZCDzrHOemCx8t4UVRsPKIKff6xHsShZCrkE3mWNqS21TfhZCxjQZDZD' # access token for use with all api calls
	creds['client_id'] = '642835651339556 ' # client id from facebook app IG Graph API Test
	creds['client_secret'] = '1614ff2c48d9822b1caf9ce5672fe49d' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v6.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['page_id'] = 'FB-PAGE-ID' # users page id
	creds['instagram_account_id'] = 'INSTAGRAM-BUSINESS-ACCOUNT-ID' # users instagram account id
	creds['ig_username'] = 'IG-USERNAME' # ig username

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print ("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty'] )# display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli
     
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