# Numeros de Python

## Numeros de Python

Hay tres tipos de numéricos en Python:

- **_int_**
- **_float_**
- **_complex_**

Las variables de tipo numérico se crean cuando les asignas un valor:

### Ejemplo

```python
x = 1   # int
x = 2.8 # float
x = 1j  # complex
```

Para verificar el tipo de cualquier objecto en Python, use la funcion `type()`:

### Ejemplo

```python
print(type(x))
print(type(y))
print(type(z))
```

## Int

Int, o entero, es un numero entero, positivo o negativo, sin decimales, de longitud ilimitada.

### Ejemplo

Enteros:

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

## Float

Float, o "numero de punto flotante" es un numero, positivo o negativo, que contiene uno o mas decimales

### Ejemplo

Flotantes:

```python
x = 1.10
y = 1.0
z = -35.39

print(type(x))
print(type(y))
print(type(z))
```

El float tambien puede ser un numero cientifico con una "e" para indicar la potencia de 10.

### Ejemplo

Flotantes:

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

## Complejo

Los numeros complejos se escriben con una "j" como parte imaginaria:

### Ejemplo

Complejos:

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

## Conversion de tipo

Puede convertir de un tipo a otro con los metodos **_int()_**, **_float()_** y **_complex()_**.

### Ejemplo

Convertir de un tipo a otro:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Convertir int a float
a = float(x)

#Convertir float a int:
b = int(y)

#Convertir int a complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

## Numero aleatorio

Python no tiene uan función `random()` para hacer un numero aleatorio, pero Python tiene un modulo integrado llamado `random` que se puede usar para generar numeros aleatorios:

### Ejemplo

Importe el modulo aleatorio y muestre un numero entre el 1 y el 9:

```python
import random

print(random.randrange(1, 10))
```

En nuestra Referencia al modulo aleatorio **_(link disponible mas adelante)_**, aprendera más sobre el módulo aleatorio.
