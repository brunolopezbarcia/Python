# Python - Fundición

## Especificar un tipo de variable

Puede haber ocasiones en las que desee especificar un tipo de variable. Esto se puede hacer con fundición. Python es un lenguaje orientado a objetos y, como tal, utiliza clase para definir tipos de datos, incluidos sus tipos primitivos.

Por lo tanto, la conversión en python se realiza mediante funciones de constructor:

- `int()`: Construye un número entero a partir de un literal entero, un literal flotante(eliminando todos los decimales) o un literal de cadena(siempre que la cadena represente un numero entero)
- `float()`: Construye un numero flotante a partir de un literal entero, un literal flotante o un literal de cadena(siempre que la cadena represente un flotante o un entero)
- `str()`: Construye una cadena a partir de una amplia variedad de tipos de datos, incluidas cadenas, literales enteros y literales flotantes.

### Ejemplo

Enteros:

```python
x = int(1)      # x va a ser 1
y = int(2.8)    # y va a ser 2
z = int("3")    # z va a ser 3
```

### Ejemplo

Flotantes:

```python
x = float(1)      # x va a ser 1.0
y = float(2.8)    # y va a ser 2.8
z = float("3")    # z va a ser 3.0
w = float("4.2")  # w va a ser 4.2
```

### Ejemplo

Str:

```python
x = str("s1")   # x va a ser 's1'
y = str(2)      # y va a ser '2'
z = str(3.0)    # z va a ser '3.0'
```