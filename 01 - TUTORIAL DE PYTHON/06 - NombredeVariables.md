# Python - Nombre de variables

## Nombre de variables

Una variable puede tener un nombre corto (como x o y) o un nombre mas descriptivo (edad, nombre del coche, volumen_total). Reglas para las variables de Python:

- Un nombre de variable debe de comenzar con una letra o el caracter de subrayado.
- Un nombre de variable no puede comenzar con un numero.
- Un nombre de variable solo puede contener caracteres alfanumericos y guiones bajos (Az, 0-9 y \_)
- Los nombres de varibales distiguen entre mayusculas y minusculas (edad, Edad y EDAD son tres variables diferentes)

### Ejemplo

Nombre de variables legales:

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Ejemplo

Nombre de variables ilegales:

```python
2myvar = "John"
my-var = "John"
my var = "John"
```

_Recuerda que los nombres de variables distiguen entre mayusculas y minusculas_

## Nombres de variables de varias palabras

Los nombres de variables con mas de una palabra pueden ser dificiles de leer.

Hay varias tecnicas que puede utilizar para hacerlos mas legibles:

### El caso de Carmel

Cada palabra, excepto la primera, comienza con una letra mayuscula.

```python
myVariableName = "John"
```

### Caso Pascual

Cada palabra comienza con una letra mayuscula:

```python
MyVariableName = "John"
```

### Caso de serpiente

Cada palabra esta separada por un caracter de subrayado:

```python
my_variable_name = "John"
```
