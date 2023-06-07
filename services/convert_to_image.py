import base64
import os

#Codificar imagenes en formato base64

def convert_to_image_base64(file_Path):
    
    #Mapeo la ruta donde estan almacenadas las imagenes 
    project_folder = os.getcwd()
    images_folder = os.path.join(project_folder,"images64")
    
    #Ejecuto la codificación de las imagenes   
    with open(file_Path,'rb') as image:
        encoded_image = image.read()
        image_base64 = base64.b64encode(encoded_image).decode('utf-8')
    return image_base64



#Decodificar imagenes de base64 a imagen
def convert_base64_to_image(base64_file, output_path):
    image_data = base64.b64decode(base64_file)

    #Obtengo ruta para la carpeta images
    project_folder = os.getcwd()
    image_folder = os.path.join(project_folder, "images")
    
    #Creo la carpeta images, en caso de no existir 
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    #Guardo la imagen en la carpeta images 
    image_path = os.path.join(image_folder, output_path)
    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)



