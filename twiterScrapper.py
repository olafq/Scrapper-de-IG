from funcionesTwiter import *

# Llama a la función para contar archivos .txt para poder ingresar a todos los twiter de ig
usuariosDeTw = contar_archivos_txt("C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\twiter\\twiterUser" )
contadorDeExcelsTw = usuariosDeTw
ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\UsuariosABuscarTw.txt")
usuariosABuscar = traer_usuarios_a_buscar(ruta_completa)
# Para TW
for i in range(1, usuariosDeTw+1):
    ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\querolol\\Desktop\\webScrapper\\WebScraperDanone\\twiter\\twiterUser\\User"+ str(i) +".txt")
    f = open(ruta_completa, "r")
    us = f.readline().strip()
    pas = f.readline().strip()
    driver = Ingresar_a_twiter(us,pas)
    #hasta aca clickea en el buscador 
    obtener_twits(driver,usuariosABuscar)
    cerrrarNavegador(driver)
