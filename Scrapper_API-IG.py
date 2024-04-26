import requests

# Token de acceso
access_token = 'EAAJIp9alpSQBO849MhMdseOcb00bnO0H60Gpzd26VPuTWkIQx79qTjwbg2K1c5e39kHmHx2OZBkJgLGw7gcrsd3V6xTAgnFyRIjMqrVPIn7FaA8t2YvBYSJ6XHQ6GJ6rjfQ7h6vuKZCJ0d6unA2ZB7bqdirXvBIjAd1gMKObjqJO0NTmvpsPoqsDqdLItIBGZBIwLjZAxcZCMQwP1Wd1NYiTEKcZAk3DOiL'

# IDs de las publicaciones
post_ids = ["18291229885134271", "17940950399706691"]

# Lista para almacenar las URL de las imágenes
image_urls = []

# Iterar sobre los IDs de las publicaciones
for post_id in post_ids:
    # URL de la solicitud
    url = f"https://graph.facebook.com/v19.0/{post_id}?fields=media_type,media_url&access_token={access_token}"
    
    # Realizar la solicitud GET
    response = requests.get(url)
    
    # Parsear la respuesta JSON
    data = response.json()
    
    # Verificar si la publicación es una imagen y obtener la URL de la imagen
    if 'media_type' in data and data['media_type'] == 'IMAGE':
        image_url = data['media_url']
        image_urls.append(image_url)

# Descargar las imágenes
for i, image_url in enumerate(image_urls):
    response = requests.get(image_url)
    with open(f"image_{i}.jpg", "wb") as f:
        f.write(response.content)


'''
import requests

def search_account(access_token, account_name):
    # URL de la solicitud para buscar la cuenta por su nombre
    url = f"https://graph.facebook.com/v19.0/{account_name}?fields=id&access_token={access_token}"
    
    # Realizar la solicitud GET
    response = requests.get(url)
    
    # Parsear la respuesta JSON
    data = response.json()
    
    # Verificar si se encontró la cuenta
    if 'id' in data:
        account_id = data['id']
        return account_id
    else:
        return None

def get_account_images(access_token, account_id):
    # URL de la solicitud para obtener las imágenes de la cuenta
    url = f"https://graph.facebook.com/v19.0/{account_id}/media?fields=id,media_url&access_token={access_token}"
    
    # Realizar la solicitud GET
    response = requests.get(url)
    
    # Parsear la respuesta JSON
    data = response.json()
    
    # Verificar si se encontraron imágenes
    if 'data' in data:
        images = []
        for item in data['data']:
            if 'media_url' in item:
                images.append(item['media_url'])
        return images
    else:
        return None

# Token de acceso
access_token = 'EAAJIp9alpSQBO849MhMdseOcb00bnO0H60Gpzd26VPuTWkIQx79qTjwbg2K1c5e39kHmHx2OZBkJgLGw7gcrsd3V6xTAgnFyRIjMqrVPIn7FaA8t2YvBYSJ6XHQ6GJ6rjfQ7h6vuKZCJ0d6unA2ZB7bqdirXvBIjAd1gMKObjqJO0NTmvpsPoqsDqdLItIBGZBIwLjZAxcZCMQwP1Wd1NYiTEKcZAk3DOiL'

# Nombre de la cuenta que deseas buscar
account_name = 'yogurisimoargentina'

# Buscar la cuenta por su nombre
account_id = search_account(access_token, account_name)

if account_id:
    # Obtener las imágenes de la cuenta
    images = get_account_images(access_token, account_id)
    if images:
        print("Imágenes encontradas:")
        for image_url in images:
            print(image_url)
    else:
        print("No se encontraron imágenes para esta cuenta.")
else:
    print("No se encontró ninguna cuenta con ese nombre.")

'''