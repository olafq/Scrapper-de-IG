from funcionesInstagram import *

# Llama a la función para contar archivos .txt para poder ingresar a todos los usuarios de ig
usuariosDeInstagram = contar_archivos_txt("C:\\Users\\Olaf\\Desktop\\Trabajo\\Scrapper-de-IG\\instagram\\instagramUser" )
contadorDeExcelsIg = usuariosDeInstagram


    
# Para IG
for i in (1,usuariosDeInstagram):
    #usuarios_a_buscar
    ruta_completa = os.path.join(os.getcwd(), "C:/Users/Olaf/Desktop/Trabajo/Scrapper-de-IG/UsuariosABuscar.txt")
    # Abre el archivo de texto en modo lectura
    with open(ruta_completa, "r") as archivo:
        usuariosABuscar = []
        # Itera sobre cada línea del archivo
        for linea in archivo:
            # Elimina espacios en blanco al principio y al final de la línea
            usuario = linea.strip()
            # Agrega el usuario a la lista
            usuariosABuscar.append(usuario)


    # Obtén la ruta completa al archivo de texto
    ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\Olaf\\Desktop\\Trabajo\\Scrapper-de-IG\\instagram\\instagramUser\\instagramUser"+ str(i) +".txt")
    f = open(ruta_completa, "r")
    us = f.readline().strip()
    pas = f.readline().strip()
    driver = Ingresar_a_instagram(us,pas) 
    '''
    nombres_usuarios = Ingresar_a_MD(driver)
    obtenerMensajesDirectosExcel(driver,nombres_usuarios,i)
    
        posts = Ingresar_a_Posts(driver,us)
        Obtener_Comentarios_del_post(driver,posts,us)
        time.sleep(10)
    '''
    buscarUsuarios(driver,usuariosABuscar)
    
    cerrrarNavegador(driver)
