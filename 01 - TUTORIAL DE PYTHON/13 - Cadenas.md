# Python - Cadenas

## STR

Las cadenas en python están entre comillas simples o comillas dobles.

`'hola'` es lo mismo que `"hola"`

Puede moster un literal de cadena con la funcion `print()`

### Ejemplo
```python
print('Hello')
print("Hello")
```

## Asignar cadena a una variable

La asignación de una cadena a una variable se realiza con el nombre de la variable seguido de un signo igual y la cadena:

```python
a = "Hello"
print(a)
```

## Cadenas multilineas

Puede asignar una cadena de varias líneas a una variable usando tres comillas:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

O tres comillas simples 
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

---

**_NOTA:_** en el resultado, los saltos de línea se insertan en la misma posición que en el codigo

---

## Las cadenas son matrices

Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres Unicode.

Sin embargo, Python no tiene un tipo de datos de caracteres, un solo caracter es simplemente unca cadena con una longitud de 1.

Se pueden usuar corchetes para acceder a elementos de la cadena.

### Ejemplo

Obtenga el caracter en la posición 1(recuerde que el primer carácter tiene la posición 0):

```python
a = "Hello, World"
print(a[1])
```

## Bucle a través de una cadena

Dado que las cadenas son matrices, podemos recorrer los caracteres de una cadena, con un bucle `for`.


### Ejemplo
Reposa las letras de la palabra "banana":

```python
for x in "banana":
    print(x)
```

Obtenga mas información sobre los bucles en el capitulos Bucles de Python(link por poner.)

## Longitud de la cadena

Para obtener la longitud de una cadena, usa la función `len()`

### Ejemplo

La función `len()` devuelve la longitud de una cadena:

```python
a = "Hello, World"
print(len(a))
```

## Comprobar cadena 
Para verificar si una determinada frase o caracter está presente en una cadena, podemos usar la palabra clave `in`


### Ejemplo

Comprueba si "free" está presente en el siguiente texto:

```python
txt = "The best things in life are free!"
print("free" in txt)
```

Usalo en una declaración `if`

### Ejemplo

Comprueba si "free" está presente en el siguiente texto:

```python
txt = "The best things in life are free!"

if "free" in txt:
    print("Yes, 'free' is present")
```

Obtenga mas información sobre las sentencias If en el capitulo Python If...Else(link por poner.)

## Comprobar si no esta

Para verificar si una determinada frase o caracter *NO* esta presente en una cadena, podemos usar la palabra clave `not in`

### Ejemplo

Comprueba si "expensive" *NO* está presente en el siguiente texto:

```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

Usalo en una declaración `if`

### Ejemplo

Imprima solo si "expensive" *NO* esta presente:

```python
txt = "The best things in life are free!"

if "expensive" not in txt:
    print("No, 'expensive' is NOT present")
```
