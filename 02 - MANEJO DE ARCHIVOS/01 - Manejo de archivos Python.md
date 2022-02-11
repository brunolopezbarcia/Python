# Arbir archivo de Python

El manejo de archivos es una parte de cualquier aplicac
Python tiene varias funciones para crear, leer, actualizar y eliminar archivos.

## Manejo de archivos.

La funcion clave para trabajar con archivos Python es la funcion **open()** .

La funcion **open()**  toma dos parametros; nombre del archivo y modo.

Hay cuatro metosdos(modos) de abrir un archivo:

```txt
"r" - Leer - Valor por defecto. Abre un archivo para la lectura, devuelve un error si el archivo no existe.
"a" - Agregar: abre un archivo para agregar, crea el archivo si no existe
"w" - Escribir: abre un archivo para escribir, crea el archivo si no existe.
"x" - Crear: crea el archivo especificado,devuelve un error si el archivo existe
````

Ademas, puede especificar si el archivo debe manejarse como modo binario o de texto

```txt
"t" - Texto - Valor por defecto. Modo de texto
"b" - Binario - Modo binario (por ejemplo, imagenes)
````
## Sintaxis

Para abrir un archivo para leerlo, basta con especificar el nombre del archivo

```python
f = open("demofile.txt")
````

El codigo anterior es el mismo que:

```python
f = open("demofile.txt", "rt")
````

Debido a que "r" para leer y "t" para texto son valores predeterminados, no necesita especificarlos. 