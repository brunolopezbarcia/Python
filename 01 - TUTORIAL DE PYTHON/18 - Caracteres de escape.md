# Python - Caracteres de escape

## Caracteres de escape

Para insertar caracteres que no son validos en una cadena, utilice un caracter de escape:

Un caracter de escape es una barra invertida `\` seguida del caracter que desea insertar.

Un ejemplo de caracter ilegal es una comilla doble dentro de una cadena que esta entre comillas dobles:

### Ejemplo

Obtendra un error si usa comillas dobles dentro de una cadena que esta entre comillas dobles:

```python
txt = "We are the so-called "Vikings" from the north."
```

Para solucionar este problema, utilice el caracter de escape `\`:

### Ejemplo

El caracter de escape le permite usar comillas dobles cuando normalmente no se pueden usar:

```python
txt = "We are the so-called \"Vikings\" from the north."
```

## Caracteres de escape

Otros caracteres de escape son:

| Codigo | Resultado       |
| ------ | --------------- |
| \'     | Single Quote    |
| \\     | Backslash       |
| \n     | New Line        |
| \r     | Carriage Return |
| \t     | Tab             |
| \b     | Backspace       |
| \f     | Form Feed       |
| \v     | Vertical Tab    |
| \ooo   | Octal           |
| \xhh   | Hexadecimal     |
| \uhhhh | Unicode         |
