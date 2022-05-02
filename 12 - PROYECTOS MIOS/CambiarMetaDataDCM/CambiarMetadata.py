import os
import pydicom
import sys
import json
from pydicom import dcmread
from pydicom.data import get_testdata_file
from pydicom.datadict import dictionary_VR
from datetime import datetime


files_path = input("Enter the path of the files:(./ si estan en este directorio) ")
contenido = os.listdir(files_path)
date = datetime.today().strftime('%Y-%m-%d')
for fichero in contenido:
    fichero2 = fichero
    ficherosinextes = fichero.split('.')[-2]
    file_path_json= "./json/"
   

    if fichero.endswith(".dcm"):
        with open(file_path_json+ficherosinextes+".json", encoding="UTF-8") as file:
            data = json.load(file)
        ds = dcmread(fichero)
        #Añade el Study Name; le ponemos el mismo nombre que el fichero
        ds.add_new(0x00081030,'LO',ficherosinextes)
        ds.add_new(0x00080060,'CS','CT') #Debiria de ser OP pero si no deja verlas en el xnat.
        ds.add_new(0x00204000,'LT',data)
        ds.add_new(0x00100010,'PN','PruebaOftalmologia')
        ds.add_new(0x00080020,'DA',date)
        ds.save_as(ficherosinextes+"nuevosmetadatos"+".dcm")
        #ds.add_new([0x0020, 0x4000],"LT",fichero.json)
       
       #Imprime en un archivo todos los metadatos del fichero.dcm
        file_path = fichero+".txt"
        sys.stdout = open(file_path, "w")
        print(ds)
    else:
        print("No es un fichero dcm")
        continue

