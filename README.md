# Convertidor de Imágenes a Base64

Este es un proyecto en Python que te permite convertir imágenes en formato base64 y también convertir base64 a imágenes.

<a href="Documentación"><img src="https://img.shields.io/badge/Doc-Actualizada-informational"></a>
<a href="Status"><img src="https://img.shields.io/badge/Status-Success-success"></a>
<a href="Lenguaje"><img src="https://img.shields.io/badge/Lenguaje-Java-blue"></a>
<a href="License"><img src="https://img.shields.io/badge/License-MIT-important"></a>

## Instalación

1. Navega al directorio del proyecto:
```bash
cd <ubicación_local>
```

2. Clona el repositorio:
```bash
git clone https://github.com/jtorrpab/base64-image-encoder.git
```
3. Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv env
source env/bin/activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Conexión a la base de datos:
```bash
Configurar datos de conexión en el archivo archivo config.son
```
## Uso
El proyecto esta conectado a una base de datos MySQL creada en phpMyAdmin, allí se almacenan los registros de las imagenes que se convierten a base64 y de allí se toman las imagenes en base64 y se decodifican en imagenes.

- Para convertir una imagen a base64 se debe subir la imagen que se desea convertir a la carpeta **images64** y luego llamar la función **loop_convert_to_image_base64("<image_name>")** y pasarle como parametro el nombre de la imagen que subiste a la carpeta **images64**.

- Para decodificar una imagen en formato base64 a imagen, esta debe estar almacenada en la base de datos y llamar la función **loop_convert_base64_to_image(id_image)**, y pasarle como parametro el id de la imagen en la base de datos, esta función se encargará de tomar la el string y convertirlo a imagen, para luego guardarlo en la carpeta **images** con la extensión jpeg, si deseas cambiar la extensión se debe modificar la linea 22  de la función loop_convert_base64_to_image().

## Contribución

Si deseas contribuir a este proyecto, no dudes en hacer un fork a este proyecto.

## License
[MIT](https://choosealicense.com/licenses/mit/)
