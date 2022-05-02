# Python - Operadores

## Operadores de Python

Los operadores se utilizan para realizar operaciones en variables y valores.

En el siguiente ejemplo, usamos el operador **+** para sumar dos valores.

```python
print(1 + 2)
```

Python divide a los operadores en los siguientes grupos:

- Operadores aritméticos.
- Operadores de asignación.
- Operadores de comparación.
- Operadores logicos.
- Operadores de identidad.
- Operadores de membresía.
- Operadores bit a bit.

## Operadores aritméticos de Python

Los Operadores aritmeticos se utilizan con valores numericos para realizar operaciones matematicas comunes.

| Operador | Nombre             | Ejemplo  |
| -------- | ------------------ | -------- |
| +        | Adicion            | x + y    |
| -        | Sustraccion        | x - y    |
| \*       | Multiplicacion     | x \* y   |
| /        | Division           | x/y      |
| %        | Modulo             | x % y    |
| \*\*     | Exponente          | x \*\* y |
| //       | Dividision de Piso | x // y   |

## Operadores de Asignacion de Python

Los operadors de asignacion se utilizan para asignar valores a la variable:

| Operador | Ejemplo  | Lo mismo que |
| -------- | -------- | ------------ |
| =        | x=5      | x=5          |
| +=       | x +=3    | x = x + 3    |
| -=       | x -=3    | x = x - 3    |
| \*=      | x \*=3   | x = x \* 3   |
| /=       | x /=3    | x = x / 3    |
| %=       | x %=3    | x = x % 3    |
| //=      | x //=3   | x = x // 3   |
| \*\*=    | x \*\*=3 | x = x \*\* 3 |
| &=       | x &=3    | x = x & 3    |
| \\|=     | x \\|=3  | x = \\| 3    |
| ^=       | x ^=3    | x = x ^ 3    |
| >>=      | x >>=3   | x = x >> 3   |
| <<=      | x <<=3   | x = x << 3   |

## Operadores de comparacion de Python

Los operadores de comparacion se utilizan para comparar dos valores:

| Operador | Nombre            | Ejemplo |
| -------- | ----------------- | ------- |
| ==       | Igual a           | x == y  |
| !=       | No igual a        | x != y  |
| >        | Mayor que         | x > y   |
| <        | Menor que         | x < y   |
| >=       | Mayor o igual que | x >= y  |
| <=       | Menor o igual que | x <= y  |

## Operadores logicos de Python

Los operadores logicos se utilizan para combinar sentiencias condicionales

| Operador | Descripcion                                                   | Ejemplo           |
| -------- | ------------------------------------------------------------- | ----------------- |
| and      | Devuelve `True` si las dos condiciones son verdaderas         | x < 5 and x < 10  |
| or       | Devuelve `True` si una de las  dos condiciones son verdaderas | x < 5 and x < 4   |
| not      | Resultado inverso, devuelve `False` si el resultado es true   | not(x<5 and x<10) |

## Operadores de identidad de Python

Los operadores de identidad se utilizan para comparar los objectos, no si son iguales, sino si en realidad son el mismo objeto, con la misma ubicacion de memoria.

| Operador | Descripcion                                                       | Ejemplo    |
| -------- | ----------------------------------------------------------------- | ---------- |
| is       | Devuelve `True` si las dos variables son el mismo objeto          | x is y     |
| is not   | Devuelve `True` si las dos variables **_NO_** son el mismo objeto | x is not y |

## Operadores de membresia de Python

Los operadores de membresia se utilizan para probar si una secuencia se presenta en un objeto:

| Operador | Descripcion                                                                                   | Ejemplo    |
| -------- | --------------------------------------------------------------------------------------------- | ---------- |
| in       | Devuelve `True` si la secuencia con el valor especificado esta presente en el objeto          | x in y     |
| not in   | Devuelve `True` si la secuencia con el valor especificado **_NO_** esta presente en el objeto | x not in y |

## Operadores bit a bit de Python

Los operadores se utilizan para comparar numeros(binarios):

| Operador | Nombre               | Descripcion                                                                                             |
| -------- | -------------------- | ------------------------------------------------------------------------------------------------------- |
| &        | AND                  | Establece el bit en 1 si ambos bits son 1                                                               |
| \\|      | OR                   | Establece el bit en 1 si uno de los dos bits es 1                                                       |
| ^        | XOR                  | Establece el bit en 1 si solo uno de los dos bits es 1                                                  |
| ~        | NOT                  | Invierte todos los bits                                                                                 |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |