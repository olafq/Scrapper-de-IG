from funcionesInstagram import *


# Llama a la función para contar archivos .txt para poder ingresar a todos los usuarios de ig
usuariosDeInstagram = contar_archivos_txt("C:\\Users\\Olaf\\Desktop\\Trabajo\\Scrapper-de-IG\\instagram\\instagramUser")
contadorDeExcelsIg = usuariosDeInstagram

# Para cada cuenta de Instagram
for i in range(1, usuariosDeInstagram + 1):  # Utiliza range() para iterar sobre los índices
    # Obtén las credenciales de la cuenta de Instagram
    ruta_completa = os.path.join(os.getcwd(), f"C:\\Users\\Olaf\\Desktop\\Trabajo\\Scrapper-de-IG\\instagram\\instagramUser\\instagramUser{i}.txt")
    with open(ruta_completa, "r") as f:
        us = f.readline().strip()
        pas = f.readline().strip()

    # Obtén todas las publicaciones de la cuenta
    params = getCreds()  # Obtén las credenciales de la API Graph
    params['debug'] = 'no'  # Establece el modo de depuración
    response = getUserMedia(params)  # Obtiene las publicaciones de la cuenta
    print(f"\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> PAGE 1 <<<<<<<<<<<<<<<<<<<<\n")  # Muestra la página 1 de las publicaciones
    print(response['json_data'])
    # Itera sobre las publicaciones de la página 1
    for post in response['json_data']['data']:
        print("\n\n---------- POST ----------\n")  # Encabezado del post
        print("Link to post:")  # Etiqueta
        print(post['permalink'])  # Enlace al post
        print("\nPost caption:")  # Etiqueta
        print(post['caption'])  # Leyenda del post
        print("\nMedia type:")  # Etiqueta
        print(post['media_type'])  # Tipo de media
        print("\nPosted at:")  # Etiqueta
        print(post['timestamp'])  # Fecha de publicación

    # Obtiene la siguiente página de publicaciones si existe
    while 'paging' in response['json_data'] and 'next' in response['json_data']['paging']:
        params['debug'] = 'no'  # Establece el modo de depuración
        response = getUserMedia(params, response['json_data']['paging']['next'])  # Obtiene la siguiente página de publicaciones
        print(f"\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> NEXT PAGE <<<<<<<<<<<<<<<<<<<<\n")  # Muestra la siguiente página de publicaciones

        # Itera sobre las publicaciones de la página actual
        for post in response['json_data']['data']:
            print("\n\n---------- POST ----------\n")  # Encabezado del post
            print("Link to post:")  # Etiqueta
            print(post['permalink'])  # Enlace al post
            print("\nPost caption:")  # Etiqueta
            print(post['caption'])  # Leyenda del post
            print("\nMedia type:")  # Etiqueta
            print(post['media_type'])  # Tipo de media
            print("\nPosted at:")  # Etiqueta
            print(post['timestamp'])  # Fecha de publicación

