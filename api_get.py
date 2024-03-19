
import requests
import json
	
def get_aves_data(api_url):
    """ 
    Función que permite obtener los datos de la api a un repositorio
    """
    response = requests.get(api_url)
    #consulta valides de los datos antes de cargar los datos
    if response.status_code == 200:
         aves_data = response.json()

    return aves_data
   

