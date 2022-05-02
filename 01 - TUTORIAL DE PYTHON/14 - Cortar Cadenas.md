# Python - Cortar Cadenas

## Dividir

Puede devolver un rango de caracteres utilizando la sintaxis de división.

Especifique el índice inicial y el índice final, separados por dos puntos, para devolver una parte de la cadena.

### Ejemplo

Obtenga los caracteres de la posición 2 a la 5(no incluidos):

```python
b = "Hello, World!"
print(b[2:5])
```

---

**_NOTA:_** El primer carácter tiene el indice 0

---

## Cortar desde el principio

Al omitir el indice de inicio, el rango comenzará en el primer carácter:

### Ejemplo

Consigue los caracteres desde el inicio hasta la posición 5(no incluido):

```python
b = "Hello, World!"
print(b[:5])
```


## Cortar hasta el final

Al omitir el indice final, el rango irá hasta el final:


### Ejemplo

Consigue los caracteres desde la posición 2 y hasta el final

```python
b = "Hello, World!"
print(b[2:])
```

## Indexación Negativa

Utilice índices negativos para indicar el segmento desde el final de la cadena

### Ejemplo

Consigue los caracteres:

- De: "o" en "Mundo"(posicion -5)
- Para, pero no incluido: "d" en "Mundo!"(posicion -2):

```python
b = "Hello, World!"
print(b[-5:-2])
```

