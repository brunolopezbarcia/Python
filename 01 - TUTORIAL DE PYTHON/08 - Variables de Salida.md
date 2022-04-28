# Python - Variables de Salida

## Variables de salida

La función de Python `print()` se usa a menudo para generar variables

### Ejemplo

```python
x = "Python is awesome"
print(x)
```
La función `print()`, genera múltiples varibales, separadas por comas:

### Ejemplo

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```
Tambien se puede usar el *+* como operador para genera multiples variables:

### Ejemplo

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

Observe el carácter de espacio después de *"Python "* y *"is "*, sin ellos el resultado sería *"Pythonisawesome"*.


Para numeros, el caracter *+* funciona como un operador matematico:

### Ejemplo

```python
x = 5
y = 10
print(x + y)
```

En la función `print()`, cuando intenta combinar una cadena y un numero con el operador *+*, Python da un error:

### Ejemplo

```python
x = 5
y = "John"
print(x + y)
```

La mejor manera de generar múltiples variables en la función `print()` es separarlas con comas, que incluso admiten diferentes tipos de datos:

### Ejemplo

```python
x = 5
y = "John"
print(x, y)
```