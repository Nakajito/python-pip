# importamos la libreria requests
import requests

# se crea una función para obtener los datos de un api
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #se escribe la dirección de la cual se va a consumir los datos
    print (r.status_code) # imprime el estado de la conexión (200 = ok)
    categories = r.json() # convertimos el string obtenido a formato json
    for category in categories: # recorremos el json en categorias
        print(category['name']) # imprimir solo el nombre de las categorias