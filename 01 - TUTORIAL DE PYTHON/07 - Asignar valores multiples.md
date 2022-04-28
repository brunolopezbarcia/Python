# Python - Asignar valores Multiples

## Muchos valores para muchas variables

Python permite asignar valores a multiples variables en una linea:

### Ejemplo

```python
x,y,z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)
```
## Un valor para múltiples variables

Se puede asignar el _mismo_ valor a multiples variables en una sola linea:

### Ejemplo

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

## Desempaquetar una colección

Si tiene una colección de valores en una lista, etc. Python permite extraer los valores en variables. Esto se llama _desempaquetar_.

### Ejemplo

```python
fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

Obtenga más información sobre cómo desempaquetar en el capítulo Desempaquetar tuplas.