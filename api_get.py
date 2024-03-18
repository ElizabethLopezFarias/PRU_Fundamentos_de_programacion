
import requests
import json


#api_url = 'https://aves.ninjas.cl/api/birds'

# def request_get(url):
# 	return json.loads(requests.get(url).text)

# if __name__ == '__main__':
# 	response = request_get (url)
# 	len(response)
# 	print(response)
	
def get_aves_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
         aves_data = response.json()

    return aves_data
   

# Ejemplo de uso:
#api_url = "https://aves.ninjas.cl/api/birds"
#aves_list = get_aves_data(api_url)
#print (aves_list)
# if bird_data_list:
#     for bird_data in bird_data_list:
#         print(f"Nombre en español: {bird_data['name_spanish']}")
#         print(f"Nombre en inglés: {bird_data['name_english']}")
#         print(f"URL de la imagen: {bird_data['image_url']}")
#         print("-" * 30)
# else:
#     print("No se pudieron obtener los datos de las aves.")