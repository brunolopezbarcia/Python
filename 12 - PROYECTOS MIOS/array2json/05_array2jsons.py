import json

data = ""

#Read json array in file with UTF-8 encoding
with open('03_datos_etiquetado.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
#Iterate over json array
for i in range(len(data)):
    #Get file name
    file_name = data[i]['IDENTIFICATIVO IMAGEN']+".json"
    #Get image comments
    comments =str(data[i])
    #Save file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False)
        f.write('\n')
    print("Archivo "+file_name+" guardado")
