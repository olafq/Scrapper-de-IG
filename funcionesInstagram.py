from funcionesGenerales import * 

#funcion que ingresa usuario y contraseña del txt pasado para instagram
def Ingresar_a_instagram(us,pas): 
    #inicializo google 
    driver = inicializarChrome()
    #Iir a la pagina de instagram 
    driver.get('https://www.instagram.com/')
    ingresar_us_cont(driver,us,pas)
    #inicia sesion 
    esperar_elemento(driver, By.XPATH, '//button[@class=" _acan _acap _acas _aj1- _ap30" and @type="submit"]').click()
    #clickea el boton de ahora no
    esperar_elemento(driver, By.XPATH, '//div[@class="_ac8f"]').click()
    #clickea el boton de no recibir notificaciones
    esperar_elemento(driver,By.XPATH,'//button[@class="_a9-- _ap36 _a9_1"]').click()
    return driver

def Ingresar_a_Posts(driver,usuario):
    esperar_elemento(driver,By.XPATH, '//a[@href="/'+str(usuario)+'/"]').click()
    posts = obtener_posts(driver)
    return posts

def obtener_posts(driver):
    wait = WebDriverWait(driver, 10)
    posts = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_aagw')))
    return posts

def scroollear_hacia_abajo(driver):
    # Define una variable para realizar seguimiento de la cantidad de elementos antes del scroll
    element_count = 0
    posts = obtener_posts(driver)
    #DONE RESOLVER QUE RECORRA TODO
    while len(posts) != element_count:
        # Espera  para que carguen los elementos adicionales
        driver.implicitly_wait(5)
        # Actualiza la variable de conteo de elementos
        element_count = len(posts)
        # Realiza otro scroll hasta el final de la página
        esperar_elemento(driver, By.TAG_NAME, 'body').send_keys(Keys.END)
        driver.implicitly_wait(5)
        # Encuentra los elementos a recopilar
        posts = obtener_posts(driver)
        esperar_elemento(driver, By.TAG_NAME, 'body').send_keys(Keys.END)
  
def Ingresar_a_buscador(driver):
    time.sleep(10)
    buscador = esperar_elementos(driver, By.XPATH,'//a[@href = "#"]')
    time.sleep(5)
    buscador[0].click()
# DONE CORREGUIR EL BUSCADOR DE IG 

def buscarUsuarios(driver,usuariosABuscar):
    # Define una variable para realizar seguimiento de la cantidad de elementos antes del scroll
    element_count = 0
    usuariosABuscar.remove("")
    for usuario in usuariosABuscar:
        Ingresar_a_buscador(driver)
        time.sleep(5)
        username_input = esperar_elemento(driver,By.XPATH, '//input[@type="text"]')
        # Ingresa el nombre de usuario en el campo usuario de la web
        username_input.send_keys(usuario)
        esperar_elemento(driver,By.XPATH, '//a[@href="/'+usuario+'/"]').click()
        
        scroollear_hacia_abajo(driver)
        time.sleep(10)
        posts = obtener_posts(driver)
        time.sleep(10)
        Obtener_Comentarios_del_post(driver,posts,usuario)
        
        

def Ingresar_a_MD(driver):
    #clickea el boton de mensaje directo
    esperar_elemento(driver, By.XPATH, '//a[@href="/direct/inbox/"]').click()
    #guarda en una lista llamado usuario todos los usuarios que nos escribieron 
    nombres_usuarios = esperar_elementos(driver,By.XPATH,'//div[@role="button"  and @class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x168nmei x13lgxp2 x5pf9jr xo71vjh x1lliihq xdj266r x11i5rnm xat24cr x1mh8g0r xg6hnt2 x18wri0h x1l895ks xbbxn1n xxbr6pl x1y1aw1k xwib8y2"]')
    return nombres_usuarios

def obtener_mg_del_post(driver,post):
 return 3
def Obtener_Comentarios_del_post(driver,posts,us):
    # Creo las listas para almacenar los datos que vamos a mandar al excel
    usuarios = []  
    comentarios = []  
    mgs = []
    fechaComentario = []
    horaComentario = []
    publicaciones = []
    perfiles = []
    #recorro todos los post del perfil 
    for i in range(len(posts)):
        #entro al post 
        post = posts[i]
        driver.execute_script("arguments[0].click();", post)
        mg = esperar_elemento(driver,By.XPATH, '//section[@class="_ae5m _ae5n _ae5o"]')
        time.sleep(5)
        #me devuelve la url actual del post 
        url_de_la_publicacion = driver.current_url
        time.sleep(5)
        #obtenemos listas de usuarios que comentaron, que comentaron y su fecha y hora 
        comentario_post = esperar_elementos(driver,By.XPATH,'//div[@class="_a9zr"]')
        fechayhora_comentado = esperar_elementos(driver,By.XPATH,'//time[@class="_a9ze _a9zf"]')
        #vamos a guardar en las lsitas creadas la info recorriendo cada usuario que comento (el primero es el perfil por eso no se recorre)
        for i in range(1,len(comentario_post)):
            # Dividir el comentario en líneas (posicion 0 usuario, posicion 1 lo que comento)
            lineas_comentario = comentario_post[i].text.split('\n')
            # Obtener los atributos datetime y title
            datetime_attr = fechayhora_comentado[i].get_attribute("datetime")
            title_attr = fechayhora_comentado[i].get_attribute("title")
            # Añadir a las listas
            mgs.append(mg.text)
            usuarios.append(lineas_comentario[0])
            comentarios.append(lineas_comentario[1])
            fechaComentario.append(title_attr)
            horaComentario.append(datetime_attr)
            perfiles.append(us)
            publicaciones.append(url_de_la_publicacion)

        #cerramos la publicacion (son 7 botones que hay en la pagina en este estado, el boton 2 es el de cerrar)
        botones =  esperar_elementos(driver,By.XPATH,'//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81" and @ role="button"]')
        time.sleep(5)
        botones[1].click()

    # Crear un DataFrame
    data = {'Perfiles':perfiles, 'Publicaciones': publicaciones, 'MGs': mgs, 'Usuarios que comentaron':usuarios, 'Comentarios': comentarios, 'Fecha de comentarios': fechaComentario, 'Hora de comentarios': horaComentario}
    # vamos a la ruta que queremos 
    nombre_carpeta = "instagram\\ComentariosPost"
    generarDF(data,'comentarios_instagram'+str(us) + '.xlsx',nombre_carpeta)
        
def obtenerMensajesDirectosExcel(driver,nombres_usuarios,contadorDeExcels):
    nombres = []  # Lista para almacenar los nombres de usuario
    cantidad_de_seguidores = [] #Lista de cantidad de seguidores que tiene el usuario
    mensajes_totales = []  # Lista para almacenar todos los mensajes
    fechas_de_mensajes = []
    horarios_de_mensajes = []
    # Recorre esta lista de nombres_usuarios para obtener los mensajes
    for i in range(len(nombres_usuarios)):
        time.sleep(5)
        nombres_usuarios[i].click()
        time.sleep(5)
        # Obtenemos el nombre del usuario concreto
        usuario = esperar_elemento(driver,By.XPATH, '//span[@class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x2b8uid x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj" and @dir="auto"]')
        nombre_usuario = usuario.text.split(" · ")[0]  # Obtenemos solo el nombre de usuario
        time.sleep(5)
        cant_seguidores = obtener_cant_seguidores(driver,nombre_usuario)
        time.sleep(5)
       #acrualizamos la lista de usuarios, porque se actualizaron los elementos html
        nombres_usuarios = Ingresar_a_MD(driver)
        nombres_usuarios[i].click()
        time.sleep(5)
        # Obtenemos el horario del mensaje
        horarios = esperar_elementos(driver,By.CLASS_NAME,'xk50ysn')
        # Obtenemos los mensajes de ese usuario
        mensajes_usuario = esperar_elementos(driver,By.CLASS_NAME, 'x6prxxf')
        for cont in range(1, len(mensajes_usuario)):
            if(len(horarios) > cont):
                fechayhora_ms = horarios[cont-1].text
            else: 
                fechayhora_ms = horarios[len(horarios)-1].text
            mensaje = mensajes_usuario[cont].text
            #nos fijamos si el mensaje fue anterior a la fecha de hoy o si fue enviado hoy
            if "," in fechayhora_ms: 
                #obtiene la fecha que es lo que esta del lado izq de la ","
                fecha = fechayhora_ms.split(",")[0]
                #obtiene la fecha que es lo que esta del lado der de la ","
                hora = fechayhora_ms.split(",")[1]
            else:
                fecha = dt.now()
                hora = fechayhora_ms

            # Agregamos el nombre de usuario, su cantid de seguidores, su mensaje con su hora y fecha a las listas globales pertinentes
            nombres.append(nombre_usuario)
            mensajes_totales.append(mensaje)
            cantidad_de_seguidores.append(cant_seguidores)
            fechas_de_mensajes.append(fecha)
            horarios_de_mensajes.append(hora)
        time.sleep(5)
    # Crear un DataFrame
    data = {'Usuario': nombres,'Cantidad de seguidores': cant_seguidores,'Mensaje': mensajes_totales, 'Fecha del mensaje': fechas_de_mensajes, 'Horario del mensaje' : horarios_de_mensajes}
    nombre_carpeta = "instagram\\MD"
    generarDF(data,'MD_instagram'+str(contadorDeExcels) + '.xlsx', nombre_carpeta)
  

def obtener_cant_seguidores(driver,nombre_usuario):
    time.sleep(5)
    #ingresa al perfil del usuario que nos mando el md
    driver.get("https://www.instagram.com/"+str(nombre_usuario)+"/")
    time.sleep(5)
    # toma una lista de la cantida de publicaciones, seguidres y seguidos
    info_user = esperar_elementos(driver,By.CLASS_NAME,'_ac2a')
    # se queda con la cantidad de seguidores el 2 elemento de la lista 
    seguidores = info_user[1].text

    return seguidores

