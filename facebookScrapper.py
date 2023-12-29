from funcionesFacebook import *

# Llama a la función para contar archivos .txt para poder ingresar a todos los usuarios de ig
usuariosDeFacebook = contar_archivos_txt("C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\facebookUser" )
contadorDeExcelsIg = usuariosDeFacebook

ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\UsuariosABuscar.txt")
# Abre el archivo de texto en modo lectura
with open(ruta_completa, "r") as archivo:
    usuariosABuscar = []
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Elimina espacios en blanco al principio y al final de la línea
        usuario = linea.strip()
        # Agrega el usuario a la lista
        usuariosABuscar.append(usuario)
    
# Para facebook
for i in (1,usuariosDeFacebook):

    # Obtén la ruta completa al archivo de texto
    ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\facebookUser\\facebookUser"+ str(i) +".txt")
    f = open(ruta_completa, "r")
    us = f.readline().strip()
    pas = f.readline().strip()
    driver = Ingresar_a_facebook(us,pas) 
    