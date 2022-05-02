# Sintaxis de Python

### Ejecutar sintaxis de Python

Como aprendimos en el tema anterior, la sintaxis de Python se puede ejecutar escribiendo directamente en la linea de comandos.

```python
>>> print("Hola Mundo")
Hola Mundo
```

O creando un archivo python en el servidor, usando la extension _.py_ y ejecutandolo en la linea de comandos:

```cmd
C:\Users\Tu Nombre>python tufichero.py
```

#

### Sangria de Python

La sangria se refiere a los espacios al comienzo de un linea de codigo.

Mientras que en otros lenguajes de programacion la sangria en el codigo es solo para facilitar la lectura, la sangria en python es muy importante.

Python usa sangria para indicar un bloque de codigo.

### EJEMPLO

```python
if 5 > 2:
    print("Cinco es mayor que dos")
```

Python le dará un error si omite la sangria:

### EJEMPLO

Error de sintaxis:

```python
if 5 > 2:
print("Cinco es mayor que dos")
```

El numero de espacios depende de ti como programador pero debe de ser al menos uno.

### EJEMPLO

```python
if 5 > 2:
    print("Cinco es mayor que dos")

if 5 > 2:
        print("Cinco es mayor que dos")
```

Tienes que usar la misma cantidad de espacios ene el mismo bloque de codigo, de lo contrario, Python te dara un error:

### EJEMPLO

```python
if  5 > 2;
	print("5 es mayor que 2")
		    print("Cinco es mayor que dos")
```

#

### Variables de Python

En python, las variables se crean cuando les asignas un valor:

### EJEMPLO

Variables de Python:

```python
x=5
y="Hola Mundo"
```

Python no tiene ningun comando para declarar una variable.

Aprenderemos mas sobre variables en el tema de Variables de Python.

#

### Comentarios

Python tiene la capacidad de comentar con el proposito de la documentacion en el codigo.

Los comentarios empieza con un # y Python representa el resto de la linea como un comentario:

### EJEMPLO

Comentarios en Python:

```python
#Esto es un comentario.
print("Hola Mundo")
```
