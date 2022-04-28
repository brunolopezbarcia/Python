# Python - Variables Globales

## Variables Globales

Las variables que se crean fuera de una función(como todos los ejemplos anteriores) se conocen como variables globales.

Las variables globales pueden ser utilizadas por todos, tanto dentro como fuera de las funciones.

### Ejemplo

Crear una variable fuera de una funcion y usarla dentro de la función.
```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

Si crea una variable con el mismo nombre denro de la función, esta variable será local y solo se podra usar dentro de la función. La variable global quedará como estaba, global y con el mismo nombre

### Ejemplo

Crear una variable dentro de una función, con el mismo nombre que la variable global
```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
```

## La palabra clave global

Normalemnte, cuando se crea una variable dentro de una función, esa variable es local y solo se puede usar dentro de esa función.

Para crear una variable global dentro de una función, puede usar la palabra `global`.

### Ejemplo

Si usa la palabra clave `global`, la variable pertenece al ámbito global:

```python
def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("Python is " + x)
```

Ademas, usa la palabra `global` si desea cambir una variable global dentro de una función


### Ejemplo

Para cambiar el valor de una variable global dentro de una función, consulte la variable usando la palabra `global`:

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("Python is " + x)
```