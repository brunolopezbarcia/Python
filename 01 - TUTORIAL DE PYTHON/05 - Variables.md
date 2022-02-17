# Python Variables


## Variables

Las variables son contenedores para almacenar valores de datos

----------------------------------------------------------------

## Creaccion de variables

Python no tiene ningun comando para declarar una variable.

Una variable se crea en el momento en que se le asigna valor por primera vez.

### Ejemplo

```python
x = 5
y = "John"
print(x)
print(y)
````

No es necesario declarar las variables con ningun tipo en particular, e incluso pueden cambiar de tipo después de que se hayan establecido.

### Ejemplo

```python
x = 4 # x es de tipo int
x = "Sally" # Ahora x es de tipo str
print (x)
````

## Conversión

Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión.

### Ejemplo

```python
x = str(3) # x va a ser '3'
x = int(3) # x va a ser 3
x = float(3) # x va a ser 3.0
````

## Obtener el tipo

Puedes obtener el tipo de una variable con la funcion type().

### Ejemplo

```python
x = 5
y = "John"
print(type(x))
print(type(y))
````

## ¿Comillas simples o dobles?

Las variables de cadena se pueden declarar mediante comillas simples o dobles:

### Ejemplo

```python
x = "John"
# es lo mismo que
x = 'John'
````

## Distingue mayusculas y minusculas.

Los nombres de las variables distinguen entre mayusculas y minusculas.

```python
a = 4
A = "Sally"
# A no sobreescribira a 
````

