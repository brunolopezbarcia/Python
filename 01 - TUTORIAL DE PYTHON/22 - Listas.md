# Python - Listas

```python
my_list = [1, 2, 3, 4, 5]
```

## Lista

Las listas se utilizan para almacenar varios elemnetos en una sola variable.

Las listas son uno de los 4 tipos de datos incorporados en Python que se utilizan para almacenar colecciones de datos, son Tuple, Set y Dictionary, todos con diferentes calidades y usos.

Las listas se crean usando corchetes, los elementos de las listas se separan con comas.

### Ejemplo

Crear una lista:

```python
this_list = ["apple", "banana", "cherry"]
print(this_list)
```

## Elementos de la lista

Los elementos de la lista están ordenados, se pueden cambiar y permiten valores duplicados.

Los elementos de la lista estan indexados, el primer elemento tiene indice `[0]`, el segundo tiene indice, `[1]`, _etc...._

## Ordenado

Cuando decimos que las listas estan ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiará.

Si agrega nuevos elementos a la lista, los nuevos elementos se colocaran al final de la lista.

---

_*NOTA:*_ Hay algunos metodos de lisa que cambiaran el orden, pero en general: el orden de los elementos no cambiara.

---

## Cambiable

La lista se puede cambiar, lo que significa que podemos cambiar, agregar y eliminar elementos en una lista despues de que se haya creado.

## Permitir duplicados

Dado que las listas estan indexadas, las listas pueden tener elementos con el mismo valor:

### Ejemplo

Las listas permiten valores duplicados:

```python
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)
```

## Longitud de la lista

Para determinar cuentos elementos tiene una lista, use la funcion `len()`:

### Ejemplo

Imprime el numero de articulos en la lista:

```python
thislist = ["apple","banana","cherry"]
print(len(thislist))
```

## Elementos de la lista - Tipos de datos

Los elementos de la lista pueden ser de cualquier tipo de datos:

### Ejemplo

Tipos de datos de cadena, int y  booleanos:


```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

Una lista puede contener diferentes tipos de datos:

### Ejemplo

Una lista con cadenas, ints y  booleanos:


```python
list1 = ["abc", 34, True, 40, "male"]
```

## type()

Desde la perspectiva de Python, las listan se definen como objetos con el tipo de datos 'lista':

```
<class 'list'>
```

### Ejemplo

¿Cual es el tio de datos de una lista?

```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
```


## El `list()` constructor

Tambien es posible usar el constructor `list()` al crear una nueva lista.


### Ejemplo

Usa el constructor `list()` para hacer una lista:

```python
thislist = list(("apple","banana","cherry")) #Tiene que haber doble parentesis
print(thislist)
```

## Colecciones de Python (Matrices)

Hay cuatro tipos de datos de recopilacion en el lenguaje de programacion Python:

- **La Lista** es una coleccion ordenada y modificable. Permite miembros duplicados.
- **Tuple** es una coleccion ordenada e inmutable. Permite miembros duplicados.
- **Conjunto** es una coleccion desordenada, inmutable* y no indexada. No hay miembros duplicados.
- **El diccionario** es una coleccion ordenada** y modificable. No hay miembros duplicados

---
*\*Los elementos establecidos no se pueden cambiar, pero puede eliminar y/o agregar elementos cuando lo desee*

*\*\*A partir de la version 3.7 de Python, los diccionarios se ordenan. En python 3.6 y versiones anteriores, los diccionarios estan desordenados.*