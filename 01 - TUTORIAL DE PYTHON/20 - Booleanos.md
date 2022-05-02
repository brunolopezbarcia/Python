# Python - Booleano

Los booleanos representan uno de dos valores: True o False

## Valores Booleanos

En programación, a menudo necesitas saber si una expresion es `True` o `False`.

Puede evaluar cualquier expresion de Python y obtener una de dos respuestas, `True` o `False`.

Cuando compara dos valores, la expresion se evalua y Python devuelve un valor booleano.

### Ejemplo

```python
print( 10 > 9 )
print( 10 == 9 )
print( 10 < 9 )
```

Cuando ejecuta una condicion en una declaracion if, Python devuelve `True` o `False`:

### Ejemplo

Imprime un mensaje basado en si la condicion es `True` o `False`:

```python
a = 200
b = 33

if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")
```

## Evaluar valores y variables

La funcion `bool()` permite evaluar cualquier valor, y darte `True` o `False`.

### Ejemplo

Evaluar una cadena y un numero:

```python
print( bool("Hello"))
print( bool(10))
```

### Ejemplo

Evalua dos variables:

```python
x = "Hello"
y = 10

print( bool(x))
print( bool(y))
```

## La mayoria de valores son verdaderos

Casi cualquier valor se evalua `True` si tiene algun tipo de contenido.

Cualquier cadena es `True`, excepyo las cadenas vacias.

Cualquier numero es `True`, excepto `0` y `0.0`.

Cualquier lista, tupla, diccionario, o conjunto es `True`, excepto los vacios.

### Ejemplo

Lo siguiente devolvera `True`:

```python
bool("Hello")
bool(10)
bool([1, 2, 3])
```

## Algunos valorese son falsos

De hecho, no hay muchos valores que se evaluen como `False`, excepto valores vacios, como `()`, `[]`, `{}`, `""`, el numeros `0` y `0.0`, y el valor `None`. Y, por supuesto, el valor `False` se evalua como `False`.

### Ejemplo

Lo siguiente devolvera `False`:

```python
bool(False)
bool(None)
bool(0)
bool(0.0)
bool("")
bool(())
bool([])
bool({})
```

Un valor mas, u objeto en este caso, se evalua como `False`, y eso es si tiene un objeto que se crea a partir de una clase con una funcion `__len__` que devuelve `0` o `False`.

### Ejemplo

    
```python

class MyClass:
    def __len__(self):
        return 0
    
obj = MyClass()
print(bool(obj))
```

## Las funciones pueden devolver valores booleano

Puede crear funciones que devuelven valores booleano.

### Ejemplo

Imprime la respuesta de esta funcion:

```python
def my_function():
    return True

print( my_function() )
```

Puede ejecutar codigo basado en la respuesta boolena de una funcion:

### Ejemplo

Imprimir "¡SI!" si la funcion devuelve `True`, o "¡NO!" si devuelve `False`:

```python
def my_function():
    return True

if my_function():
    print("¡SI!")
else:
    print("¡NO!")
```

Python tambien tiene muchas funciones integradas que devuelven un valor booleano, como `isinstance()`, que se puede usar para determinar si un objeto es de cierto tipo de datos:

### Ejemplo

Compruebe si un objeto es un numero entero o no:

```python
x = 10
print( isinstance(x, int))
```


