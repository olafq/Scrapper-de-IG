from funcionesGenerales import * 

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

def Ingresar_a_twiter(us, pas):
    # Inicializa Google Chrome
    driver = inicializarChrome()
    time.sleep(5)
    
    # Ir a la página de Twitter
    driver.get('https://twitter.com/')
    
    # Esperar a que aparezca el enlace de login y hacer clic en él
    esperar_elemento(driver, By.XPATH, '//a[@href="/login"]').click()
    
    # Esperar a que aparezca el campo de nombre de usuario y escribir el nombre de usuario
    esperar_elemento(driver, By.XPATH, '//input[@autocomplete="username"]').send_keys(us)
    time.sleep(10)
    # Hacer clic en el botón de login
    esperar_elementos(driver, By.XPATH, '//div[@role="button" and @tabindex= "0"]')[2].click()
    # Esperar a que aparezca el campo de contraseña y escribir la contraseña
    esperar_elemento(driver, By.NAME, 'password').send_keys(pas)

    # Hacer clic en el botón de login
    esperar_elemento(driver, By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()

    return driver

def obtener_twits(driver, usuariosABuscar):
    for i in range(len(usuariosABuscar)-1):
        tweets_obtenidos = set()  # Crear un conjunto para evitar duplicados
        buscar_usuario(driver, usuariosABuscar[i])
        time.sleep(5)
        # clickea en Latest
        botones = esperar_elementos(driver,By.XPATH, '//div[@role="presentation"]')
        botones[2].click()
        time.sleep(5)
        obtener_posts(driver,usuariosABuscar[i], cantidad=15)
        

def saber_si_es_tw_citado(contenedor_tweet,tweetsRealizados,c,citados):
     #dividir el contenedor en lineas 
    lineasDelContenedor = contenedor_tweet.text.split('\n')
    #contar las lineas del contenedor qwue tienen "."
    conteoPuntos = 0
    for linea in lineasDelContenedor:   
        if linea.strip() == '·':
            conteoPuntos +=1
    if conteoPuntos> 1:
        citados.add(tweetsRealizados[c].text)
    return citados
    
def tweet_no_esta_en_citados(tweet,citados):
        if(tweet.text in citados):
            return False
        return True


def obtener_posts( driver,us, cantidad):
    tiempo_espera = 3
    lista_de_tweets = set()
    usuariosDelTw = []
    fechasDelTw = []
    tweets = []
    cantComentariosDelTw = []
    cantRtsDelTw =[]
    cantMgsDelTw = []
    cantViewsDelTw = []
    citados = set()
    cont = 0
    seCito = 0

    # Navega hacia abajo hasta obtener la cantidad deseada de tweets
    while len(lista_de_tweets) < cantidad:
        tweets_actuales = len(lista_de_tweets)
        # Localiza el elemento <time> en la página
        time_elements = driver.find_elements(By.XPATH, '//time')
        #lista_option = driver.find_elements(By.XPATH,'//div[@class="css-1dbjc4n r-1jkjb"]')
        contenedores_tweets = driver.find_elements(By.XPATH,'//article[@data-testid="tweet"]')
        tweetsRealizados = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
        cantRtsDelTw2 = driver.find_elements(By.XPATH,'//div[@data-testid="retweet"]')
        cantComentariosDelTw2 = driver.find_elements(By.XPATH,'//div[@data-testid="reply"]')
        cantViewsDelTw2 = driver.find_elements(By.XPATH,'//a[@class="css-175oi2r r-1777fci r-bt1l66 r-bztko3 r-lrvibr r-1ny4l3l r-1loqt21"]')
        cantMGsDelTw2 = driver.find_elements(By.XPATH,'//div[@data-testid="like" or @data-testid="unlike"]')
        usuarios = driver.find_elements(By.XPATH,'//div[@class="css-175oi2r r-1wbh5a2 r-dnmrzs"]')
        contador = 0
        usuarios_reales = []
#
#       
        for uss in usuarios:
            if uss.text!="" and  uss.text.startswith("@"):
                usuarios_reales.append(uss.text)
       
        for  usuario,time_element,contenedor_tweet,tweetRealizado, cantComentTw2,cantViewTw2,cantMgTw2,cantRTTw2 in zip(usuarios_reales,time_elements,contenedores_tweets,tweetsRealizados,cantComentariosDelTw2,cantViewsDelTw2,cantMGsDelTw2,cantRtsDelTw2): 
            
            contador = contador +1
            if len(tweetRealizado.text.strip()) != 0:
                if tweetRealizado not in lista_de_tweets:
                            idiomaDelTw = detect(tweetRealizado.text)
                            if idiomaDelTw == "es":
                                cont +=1
                                citados = saber_si_es_tw_citado(contenedor_tweet,tweetsRealizados,contador,citados)
                                
                                if tweet_no_esta_en_citados(tweetRealizado,citados):
                                    if(seCito == 0): 
                                        lista_de_tweets.add(tweetRealizado)  # Agrega el texto al conjunto si no existe en la lista de tweets
                                        tweets.append(tweetRealizado.text)
                                        
                                        
                                        fechaDelTw = time_element.get_attribute('datetime')  # Obtén el valor del atributo 'datetime'
                                        fechasDelTw.append(fechaDelTw)
                                        usuariosDelTw.append(usuario)
                                        #cantComentariosDelTw.append(cantComentTw)
                                        cantComentariosDelTw.append(cantComentTw2.text)
                                        cantMgsDelTw.append(cantMgTw2.text)
                                        #cantRtsDelTw.append(cantRTTw)
                                        cantRtsDelTw.append(cantRTTw2.text)
                                        #cantViewsDelTw.append(cantViewTw)
                                        cantViewsDelTw.append(cantViewTw2.text)
                                        
                                    else:
                                        lista_de_tweets.add(tweetsRealizados[contador].text)  # Agrega el texto al conjunto si no existe en la lista de tweets
                                        tweets.append(tweetsRealizados[contador].text)
                                        fechaDelTw = time_element.get_attribute('datetime')  # Obtén el valor del atributo 'datetime'
                                        fechasDelTw.append(fechaDelTw)
                                        # quiero que agregue el siguiente tweetRealizado al actual DONE
                                        usuariosDelTw.append(usuarios[contador])
                                        #cantComentariosDelTw.append(cantComentTw)
                                        cantComentariosDelTw.append(cantComentTw2.text)
                                        cantMgsDelTw.append(cantMgTw2.text)
                                        #cantRtsDelTw.append(cantRTTw)
                                        cantRtsDelTw.append(cantRTTw2.text)
                                        #cantViewsDelTw.append(cantViewTw)
                                        cantViewsDelTw.append(cantViewTw2.text) 
                                else:
                                    lista_de_tweets.add(tweetsRealizados[contador].text)  # Agrega el texto al conjunto si no existe en la lista de tweets
                                    tweets.append(tweetsRealizados[contador].text)
                                    fechaDelTw = time_element.get_attribute('datetime')  # Obtén el valor del atributo 'datetime'
                                    fechasDelTw.append(fechaDelTw)
                                    usuariosDelTw.append(usuarios[contador])
                                    #cantComentariosDelTw.append(cantComentTw)
                                    cantComentariosDelTw.append(cantComentTw2.text)
                                    cantMgsDelTw.append(cantMgTw2.text)
                                    #cantRtsDelTw.append(cantRTTw)
                                    cantRtsDelTw.append(cantRTTw2.text)
                                    #cantViewsDelTw.append(cantViewTw)
                                    cantViewsDelTw.append(cantViewTw2.text)
                                        
                                
        if len(lista_de_tweets) < cantidad:
            # Desplázate hacia abajo para cargar más tweets
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)

        # Espera un momento para que se carguen los nuevos tweets
        time.sleep(tiempo_espera)
        if(len(lista_de_tweets)==tweets_actuales):
            break
 

    # Crear un DataFrame
    data = {'Usuarios':usuariosDelTw, 'fecha del tw': fechasDelTw, 'tweets': tweets, 'cantViewsDelTw':cantViewsDelTw, 'cantMgsDelTw': cantMgsDelTw, 'cantRtsDelTw': cantRtsDelTw, 'cantComentariosDelTw': cantComentariosDelTw}
    # vamos a la ruta que queremos
    nombre_carpeta = "twiter\\tweets"
    generarDF(data, 'tweets_' + str(us) + '.xlsx', nombre_carpeta)
    return lista_de_tweets


def buscar_usuario(driver, usuarioABuscar):
    esperar_elemento(driver, By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]').click()

    username_input = esperar_elemento(driver, By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')
    username_input.send_keys(Keys.CONTROL + 'a')  # Seleccionar todo el texto
    username_input.send_keys(Keys.DELETE)         # Borrar el texto seleccionado

    username_input.send_keys(usuarioABuscar)
    username_input.send_keys(Keys.ENTER)


