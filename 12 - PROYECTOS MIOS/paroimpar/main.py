# Este es mi primer proyecto en python, se trata de hacer un programa que diga si es par o impar

# Primero definimos la funcion para comprobar si es par o impar
def comprobador(numero):
        if (numero%2 == 0):
            print("El numero",numero,"es par")
        else:
            print("El numero",numero, "es impar")

#Ahora le pedimos al usuario que introduzca un numero.
print("Escribe el numero que quieras comprobar si es par o impar:")
numero =int(input())

#Llamamos a la funcion que compruebe si es par o impar. Le tenemos que decir cual es la variable para comprobar.
comprobador(numero)

