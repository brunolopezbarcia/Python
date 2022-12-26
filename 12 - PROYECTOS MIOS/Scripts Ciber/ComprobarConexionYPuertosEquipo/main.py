import argparse
import os
import socket


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--servidor", type=str, help="Especifica el servidor", required=True)
parser.add_argument("-t", "--timeout", type=int, help="Especifica la pausa entre comprobaciones de puerto", required=True)
args = parser.parse_args()



servidor = args.servidor
timeout = args.timeout
respuesta = os.system("ping -c 4 " + servidor)

if respuesta == 0:
    print (servidor, "esta activo")
else:
    print(servidor, "no esta funcionando")


def comprobarPuertos():
    puerto = 1
    while puerto < 65536:
        try:
            sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            status= sock.connect_ex((servidor, puerto))

            if status == 0:
                print(f"El puerto {puerto} esta abierto -- {servidor}" )
            sock.close()

        except socket.error as err:
            print(f"Error conexion{err}")
        puerto += 1

comprobarPuertos()