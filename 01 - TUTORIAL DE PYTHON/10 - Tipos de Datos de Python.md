# Python - Tipos de Datos

## Tipos de datos incorporados

En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer diferentes cosas.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorias:

- Tipo de texto: **_str_**
- Tipos numericos: **_int_**, **_float_**, **_complex_**
- Tipos de secuencia: **_list_**, **_tumple_**, **_range_**
- Tipo de mapeo: **_dict_**
- Establecer tipos: **_set_**, **_frozenset_**
- Tipo booleano: **_bool_**
- Tipo binario: **_bytes_**, **_bytearray_**, **_memoryview_**

## Obtener el tipo de datos

Puedes obtener el tipo de datos de cualquier objeto utilizando la funcion `type()`:

### Ejemplo

Imprime el tipo de datos de la variable x:

```python
x = 5
print(type(x))
```

## Configuracion del tipo de datos.

En python, el tipo de datos se estable cuando se le asigna el valor a una variable.

| Ejemplo                                      | Tipo de Dato |
| -------------------------------------------- | ------------ |
| x="Hello World"                              | str          |
| x = 20                                       | int          |
| x = 20.5                                     | float        |
| x = 1j                                       | complex      |
| x = ["apple", "banana", "cherry"]            | list         |
| x = ("apple", "banana", "cherry")            | tuple        |
| x = range(6)                                 | range        |
| x = {"name" : "John", "age" : 36}            | dict         |
| x = {"apple", "banana", "cherry"}            | set          |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset    |
| x = True                                     | bool         |
| x = b"Hello"                                 | bytes        |
| x = bytearray(5)                             | bytesarray   |
| x = memoryview(bytes(5))                     | memoryview   |

## Configuracion del tipo de datos especifico

Si desea especificar el tipo de datos, puede utilizar las siguientes funciones:

| Ejemplo                                      | Tipo de Dato |
| -------------------------------------------- | ------------ |
| x=str("Hello World")                         | str          |
| x = int(20)                                  | int          |
| x = float(20.5)                              | float        |
| x = complex(1j)                              | complex      |
| x = list(("apple", "banana", "cherry"))      | list         |
| x = tuple(("apple", "banana", "cherry"))     | tuple        |
| x = range(6)                                 | range        |
| x = dict("name" : "John", "age" : 36)        | dict         |
| x = set(("apple", "banana", "cherry"))       | set          |
| x = frozenset(("apple", "banana", "cherry")) | frozenset    |
| x = bool(5)                                  | bool         |
| x = bytes(5)                                 | bytes        |
| x = bytearray(5)                             | bytesarray   |
| x = memoryview(bytes(5))                     | memoryview   |
