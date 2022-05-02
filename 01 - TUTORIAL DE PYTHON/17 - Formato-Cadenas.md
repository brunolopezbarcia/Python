# Python - Formato - Cadenas

## Formato de Cadena

Como aprendimos en el capitulo de Variables de Python, no podemos combinar cadenas y números como este:

### Ejemplo

```python
edad= "36"
txt = "Tengo " + edad + " años"
print(txt)
```

¡Pero podemos combinar cadenas y numeros usando el metodo `format()`!

El metodo `format()` toma los argumentos pasados, les da formato y los coloca en la cadena donde `{}` estan los marcadores de posicion:

### Ejemplo

Usa el metodo `format()` para combinar cadenas y numeros:

```python
edad = "36"
txt = "Tengo {} años".
print(txt.format(edad))
```

El metodo `format()` toma un numero ilimitado de argumentos y se colocan en los marcadores de posicion respectivos:

### Ejemplo

```python
cantidad = "10"
itemno = "1"
precio = "100"
miorden = "Quiero {} unidades de este item {} por el precio de {} euros".
print(miorden.format(cantidad, itemno, precio))
```

Puedes usar numeros de indice {0} para asegurarte de que los argumentos se colocan en los marcadores de posicion correctos.

### Ejemplo

```python
cantidad = "10"
itemno = "1"
precio = "100"
miorden = "Quiero {0} unidades de este item {1} por el precio de {2} euros".
print(miorden.format(cantidad, itemno, precio))
```

Obtenga mas informacion sobre el formato de cadenas en el capitulo Formato de Cadenas de Python(link por poner)
