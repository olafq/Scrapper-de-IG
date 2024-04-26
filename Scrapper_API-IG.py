from funcionesAPI import *

# Define la lista de usuarios
publicaciones = []
perfiles = []
ruta_completa = os.path.join(os.getcwd(), "C:\\Users\\Olaf\\Desktop\\Trabajo\\Scrapper-de-IG\\UsuariosABuscar.txt")
    # Abre el archivo de texto en modo lectura
with open(ruta_completa, "r") as archivo: 
        usuariosABuscar = []
        # Itera sobre cada línea del archivo
        for linea in archivo:
            # Elimina espacios en blanco al principio y al final de la línea
            usuario = linea.strip()
            # Agrega el usuario a la lista
            usuariosABuscar.append(usuario)

# Token de acceso
access_token = "EAAJIp9alpSQBO9oVLKtuqn8wgWakcqBU8OZBkVZARLq2hz0ugt5gJZAS90ZBWXrmEz3oecaEBNFfbCaSNZAinZA3eFgvWVZCqKlpBaeKROYXUyi4dZAYebyCqitZCCFILUstvZCqrkZBvtcs6K4sOlCmZCmynCbJKghkxGz5MsVkYDszuDOqdNZCdaAz7Ah4PsoAB1ja4LjmbDqmFRBJoIVqAZBBKuaFQDHii6owZDZD"

# Itera sobre cada usuario
for usuario in usuariosABuscar:
    url_info = f"https://graph.facebook.com/v19.0/17841462284503224?fields=business_discovery.username(danonetest){{media{{comments_count,like_count,media_url,id}}}}&access_token={access_token}"
    response_info = requests.get(url_info).json()

    # Extrae la información deseada
    #followers_count = response_info["business_discovery"]["followers_count"]
    #media_count = response_info["business_discovery"]["media_count"]
    data = response_info["business_discovery"]["media"]["data"]
    for i in data:
        comentarios = i["comments_count"]
        url = i["media_url"]
        like = i["like_count"]
        ids= i["id"]
        print(comentarios)
        print(url)
        print(like)
        print(ids)

 
    
# comentarios de cada publicacion https://graph.facebook.com/v19.0/18291229885134271/comments?access_token=EAAJIp9alpSQBO5qRMeWwq5eWxkdEoUU153FCXRhUxADZAlXsEBFNTKFVSrwZBk4Ya9p3B7BXHa2fWdU8OgCbNXrirQG5FYNjPw4dIinzAmSeMRKZAJxGhbzqy09K70y4kEZCr2EPHL8RgtxmuuOJfZAzEDvRwX6lJnqlWQo7MeZAATkfljYKqYtKEKvCwEmLZBOZAubbHg4QVHSivXTILJerDMbFMgQkugZDZD
#el id es el id del post que devuelve pero no me deja en otras cuentas agenas.....
