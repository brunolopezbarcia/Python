# Primeros Pasos con Python

### Instalacion de Python

Muchos ordenadores tanto Windows como Mac ya tendran Python instalado.

Para verificar si tiene Python instalado en su ordenador(Windows), busque Python en la barra de inicio o ejecute lo siguiente en la linea de comandos(cmd.exe):

```cmd
C:\Users\TuNombre>python --version
```

Para verificar si tiene Python instalado en Linux o Mac, en Linux tienes que abrir la linea de comando o en mac la terminal y escriba:

```cmd
python --version
```

Si descubre que no tiene Python instalado en su ordenador, puede descargarlo desde el siguiente sitio web: **https://www.python.org/**

##

### Inicio Rapido de Python

Python es un lenguaje de programacion interpretado, esto significa que, como desarrollador, escribe archivos de Python _(.py)_ en un editor de texto y luego coloca esos archivos en el interprete de Python para que se ejecuten.

La forma de ejecutar un archivo python es así en la linea de comando:

```
C:\Users\Tu Nombre>python holamundo.py
```

Donde _holamundo.py_ es el nombre de su archivo python.

Escribamos nuestro primer archivo de Python, llamado holamundo.py, que se puede hacer en cualquier editor de texto

El nombre del archivo sera: holamundo.py

El contendido sera el siguiente:

```python
print("Hola Mundo")
```

Simple como eso. Guarde su archivo. Abra su linea de comandos, navege hasta el directorio donde guardo su archivo y ejecute:

```cmd
C:\Users\Tu Nombre>python holamundo.py
```

La salida deberia de ser asi:

```
Hola Mundo
```

Felicitaciones, ya has escrito y ejecutado su primer programa en python.

#

### La linea de comandos de Python

Para probar una pequeña cantidad de codigo en python, a veces es mas rapido y facil no escribir el codigo en un archivo. Esto es posible porque Python se puede ejecutar en la linea de comandos.

Escriba lo siguiente en la linea de comandos:

```
python
```

O si el comandos "python" no funcionó, puede probar con .py:

```
py
```

Desde alli, puede escribir cualquier codigo de python, incluido nuesto ejemplo de hola mundo:

```cmd
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>print("Hola Mundo")
```

Que escribira "Hola Mundo" en la linea de comandos:

```cmd
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>print("Hola Mundo")
Hola Mundo
```

Cuando haya terminado en la linea de comandos de python, puede simplemente escribir lo siguiente para salir de la interfaz de la linea de comandos de python:

```
exit()
```
