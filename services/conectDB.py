import json
import mysql.connector


def connection():
    try:
        
        with open('./config/config.json') as file:
            config = json.load(file)
        
        cnn = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

        if cnn.is_connected():
            print("Conexión exitosa a la base de datos")
            return cnn

    except mysql.connector.Error as error:
        print("No se pudo conectar a la base de datos:", error)
        print("No se pudo conectar a la base de datos:", error)

    return None

