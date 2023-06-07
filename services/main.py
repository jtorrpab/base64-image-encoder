from datetime import datetime
import os
import conectDB
import convert_to_image
import mysql.connector

def loop_convert_base64_to_image():
    
    #Obtengo una conexión a la base de datos MySQL
    connection = conectDB.connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT image FROM py64image")
            base64_data = cursor.fetchone()
           
            imageAccount = 0
            if base64_data is not None:
                
                #Ronombrar el archivo
                imageAccount += 1
                file_name = f"image_{imageAccount}.jpeg"
                project_path= os.getcwd()
                image_path= os.path.join(project_path,"images")
                output_path = os.path.join(image_path,file_name)
                
            x = convert_to_image.convert_base64_to_image(base64_data[0],output_path)  
            save_image = lambda x: x if not None else False
            
            if save_image:
                print("Imagen convertida y guardada exitosamente")
            else:
                raise Exception ("No se pudo convertir y guardar la imagen")
            
        except mysql.connector.Error as error:
            print("Error de MySQL:", error)
        finally:
            cursor.close()
            connection.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
          

def loop_convert_to_image_base64(image_name):
    
    #Captura de la ruta de la imagen 
    project_path = os.getcwd()
    image_path = os.path.join(project_path,"images64")
    file_Path = os.path.join(image_path,image_name)
    
    image_base64 = convert_to_image.convert_to_image_base64(file_Path)
    
    if image_base64 is not None:
        connection = conectDB.connection()
        if connection is not None:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO py64image (image, creation_date) VALUES (%s, %s)", (image_base64, datetime.now().date()))
                    connection.commit()
                    print(f"la imagen {image_name} se agrego correctamente a la base de datos")
 
                except mysql.connector.Error as error:
                    print("Error de MySQL:", error)
                finally:
                    cursor.close()
                    connection.close()
        else:
            raise Exception("No se pudo establecer la conexión a la base de datos.")
    else:
        raise Exception("No se pudo convertir la imagen.")

    


#Llamado de metodos
#loop_convert_base64_to_image()
#loop_convert_to_image_base64("image_name")
