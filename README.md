# python_mutants

## Descripción del Repositorio:

Este es un repositorio con los archivos para la solución de la prueba técnica de Mercado Libre en la que se solicita desarrollar un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN. 

El desarrollo fue realizado por Oscar Rocha en el lenguaje de programación Python versión 3.11.2


## Listado de archivos:
*	app_final.py: Archivo en código Python para la ejecución de la aplicación, en donde se encuentran las diferentes APIs solicitadas en la prueba.
*	configuraciones.py: Archivo en código Python que incluye las configuraciones necesarias para la conexión a la base de datos en el servidor local, y el cual es llamado desde el archivo app_final.py
*	pruebas_funcionales.docx: Pruebas funcionales realizadas a las APIs desarrolladas en el archivo app_final.py
*	datos_pruebas.txt: DNAs utilizados en la realización de pruebas funcionales, en formato JSON para la ejecución del servicio POST solicitado en la prueba.
*	dna_verificados.sql: Estructura de la base de datos utilizada en la aplicación
*	apis_dna_meli.postman_collection: Colección de peticiones utilizados en las pruebas funcionales
*	Readme.docx: Readme más completo con imágenes

## Ejecución de la Aplicación:

Para ejecutar la aplicación, se debe contar localmente pon Python v3.11.2 y una base de datos llamada dna_verificados en MYSQL con la estructura que se encuentra incluida en el repositorio con nombre dna_verificados.sql.

a.	Para la descarga de Python dirigirse al enlace: Download Python | Python.org y buscar la versión 3.11.2

b.	Instalar Python

c.	Al instalar Python se instala una herramienta llamada “pip” que es utilizada en la instalación de paquetes.

d.	Para el correcto funcionamiento de la aplicación, se deben instalar los siguientes paquetes de Python desde cmd, ejecutando los siguientes comandos:
*	pip install Flask
*	pip install Flask-MySQLdb

e.	Para ejecutar la aplicación, en cmd desde la carpeta donde se descargó el repositorio, se ejecuta el comando:
*	python app_final.py 

Al ejecutarse la aplicación en cmd se informa la dirección ip, a la cual se puede acceder para ver los servicios. Normalmente la ip es http://127.0.0.1:5000
 

f.	Para realizar las pruebas de los servicios, se debe contar con alguna herramienta que permita realizar dichas peticiones. Se recomienda instalar Postman, el cual es un software libre.

g.	Abrir Postman y ejecutar las peticiones o por el navegador apuntando a las siguientes rutas:
*	http://127.0.0.1:5000/mutant
*	http://127.0.0.1:5000/stats

h.	En el archivo app_final.py se crearon 3 tipos de peticiones:
*	En la dirección http://127.0.0.1:5000/mutant se creó el método POST para enviar el dna en formato JSON y evaluar si el humano es mutante o no.
*	En la dirección http://127.0.0.1:5000/mutant se creó el método GET para obtener de la base de datos, todos los registros de dna de humanos que han sido evaluados.
*	En la dirección http://127.0.0.1:5000/stats se creó el método GET para obtener las estadísticas de los dna de humanos que han sido evaluados.

i.	Si es para el método POST, en postman la entrada debe ser en formato JSON con la siguiente estructura:

EJEMPLO:

{
  "dna":[
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
  ]
}

Nota: En el repositorio se encuentra el archivo datos_pruebas.txt en donde se encuentran todos los ejemplos de dna para realizar las pruebas. Igualmente se incluye la colección de las peticiones para realizar las pruebas en el archivo apis_dna_meli.postman_collection, el cual puede ser importado desde Postman, en la siguiente ruta Collections > Import > File

j.	De la siguiente manera se puede verificar el funcionamiento de la aplicación para las funcionalidades:
*	Verificar si es mutante:
**	Se selecciona cualquiera de las peticiones y dar clic en el botón Send:
POST dna_mutante1
POST dna_no_mutante1
POST dna_mutante2
POST dna_no_mutante2
POST dna_mutante3
POST dna_con_errores1
POST dna_con_errores2
**	En el cuadro inferior se observa la respuesta a la petición
Si se desea se cambia en Body el dna que se requiere evaluar y se oprime el botón Send para ver la respuesta de la petición
 
*	Verificar todos los registros dna que han sido evaluados:
**	Se selecciona la petición “GET dna_listados” y dar clic en el botón Send:

En el cuadro inferior se observa la respuesta a la petición

*	Verificar las estadísticas de los dna evaluados:
**	Se selecciona la petición “GET estadisticas” y dar clic en el botón Send:
 
En el cuadro inferior se observa la respuesta a la petición

## Pruebas

Pruebas Funcionales: En el archivo apis_dna_meli.postman_collection se encuentra el ejemplo de collect para los métodos de pruebas ejecutados sobre la aplicación.
En el archivo descargado del repositorio con nombre pruebas_funcionales.docx se encuentran las siguientes pruebas realizadas al aplicativo:
*	Evaluación letras DNA
*	Evaluación DNA mutante
*	Verificación DNA repetido
*	Validación estadísticas de API

Autor:
Esta aplicación fue realizada por Oscar Rocha como examen de Mercadolibre.

Email: oscarrca@hotmail.com
Fecha: 22/02/2023


