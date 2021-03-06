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

Tambien se puede usar el _+_ como operador para genera multiples variables:

### Ejemplo

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

Observe el carácter de espacio después de _"Python "_ y _"is "_, sin ellos el resultado sería _"Pythonisawesome"_.

Para numeros, el caracter _+_ funciona como un operador matematico:

### Ejemplo

```python
x = 5
y = 10
print(x + y)
```

En la función `print()`, cuando intenta combinar una cadena y un numero con el operador _+_, Python da un error:

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
