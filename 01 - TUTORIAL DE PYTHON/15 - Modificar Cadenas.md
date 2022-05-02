# Python - Modificar Cadenas

Python tiene un conjunto de métodos integrados que puede usar en cadenas.

## Mayusculas


### Ejemplo

El metodo `upper()` devuelve la cadena en mayusculas:

```python
a = "Hello, World!"
print(a.upper())
```

## Minuscula


### Ejemplo

El metodo `lower()` devuelve la cadena en minusculas:

```python
a = "Hello, World!"
print(a.lower())
```

## Eliminar espacios en blanco

El espacio en blanco es el espacio antes y/o despues del texto real, y muy a menudo desea eliminar este espacio.

### Ejemplo

El metodo `strip()` elimina cualquier espacio en blanco desde el principio o el final:

```python
a = " Hello, World! "
print(a.strip())    # Devuelve "Hello, World!"
```

## Reemplazar cadena

### Ejemplo

El metodo `replace()` reemplaza una cadena con otra cadena:

```python
a = " Hello, World! "
print(a.replace("H", "J"))    # Devuelve "Hello, World!"
```

## Cadena dividida
El metodo `strip()` devuelve una lista donde el texto entre el separador especificadp se convierte en los elementos de la lista:

### Ejemplo

El metodo `split()` divide la cadena en subcadenas si encuentra instancias del separador:

```python
a = " Hello, World! "
print(a.split(","))    # Devuelve ['Hello', 'World!']
```

Obtenga mas informacion sobre las lista en el capitulo Listas de Python(link por poner)

## Metodos de Cadena

Obtenga mas informacion sobre los metodos de cadena en el capitulo de Metodos de Cadena(link por poner.)