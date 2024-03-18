import requests
from api_get import get_aves_data
from string import Template

api_url = "https://aves.ninjas.cl/api/birds"
response = get_aves_data(api_url)
aves_list =[]
#recorre la base de datos para obtener sólo la información necesaria
for ave in response:
    aves_list.append((ave["images"]["main"], ave["name"]["spanish"], ave["name"]["english"]))
##style="width: 18rem;
#tenplate de card para html
template_card = """<div class="card" style="width: 18rem"> 
                <img src="$img_url" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">$nombre_esp</h5>
                    <p class="card-text">$nombre_eng</p>
                </div>
            </div>
    """

card_template = Template (template_card)
texto_img = ''
for img_url, nombre_esp, nombre_eng in aves_list:
    texto_img += card_template.substitute(img_url=img_url, nombre_esp=nombre_esp, nombre_eng=nombre_eng) + '\n'

html_template = Template('''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">                            
    <style>
        .card {
            margin: 10px; /* Margen de 10 píxeles para cada carta */
        }
        .card-img-top {
            height: 300px; /* Establece la altura deseada para las imágenes */
            object-fit: cover; /* Ajusta la imagen para que cubra el contenedor */
        }
        .container {
            align-items: center; /* Centra verticalmente el contenido */
            height: 100vh; /* Altura del 100% de la ventana */
        }
    </style>
                         
  </head>
  <body>
    <h1 class="text-center"> Aves de Chile</h1>
    <div class="container">
    <div class="row justify-content-center">
            $body
    </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body = texto_img)
print (html)
archivo =  open('catalogo.html', 'w+', encoding='utf-8')
archivo.write(html)
archivo.close()