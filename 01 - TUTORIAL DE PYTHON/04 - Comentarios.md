# Comentarios de Python

- Los comentarios se puedan usar para explicar el codigo de python
- Los comentarios se pueden utilizar para hacer que el codigo sea mas legible
- Los comentarios se pueden usar para evitar la ejecuccion al probar el codigo.

#

### Crear un comentarios

Los comentarios comienzan con un #, y Python los ignorara:

### EJEMPLO

```python
#Esto es un comentarios
print("Hola mundo")
```

Los comentarios se pueden colocar al final de una linea y Python ignorara el resto de la linea:

### EJEMPLO

```python
print ("Hola Mundo") #Esto es un comentario
```

Un comentario no tiene que ser texto que explique el codigo, tambien se puede usar para evitar que Python ejecute codigo:

### EJEMPLO

```python
#print("Hola Mundo")
print("Saludos amigo")
```

#

### Comentarios de varias lineas

Python realmente no tiene una sintaxis para comentarios de varias lineas.

Para agregar un comentario de varias lineas, puede insertar un # para cada linea:

### EJEMPLO

```python
#Esto es un comentario
#escrito en
#mas de una linea
print("Hola Mundo")
```

O, no del todo como se pretendia, puede usar una cadena de varias lineas.

Dado que Python ignorara los literales de cadena que no estan asignados a una variable, puede agregar una cadena de varias lineas (comillas dobles) en su codigo y colocar su comentario dentro de ella

### EJEMPLO

```python
"""
Esto es un comentario
escrito en
mas de una linea
"""
print("Hola Mundo")
```

Siempre que la cadena no este asignada a una variable, Python leera el codigo, pero luego lo ignorara y habra realizado un comentario de varias lineas.
