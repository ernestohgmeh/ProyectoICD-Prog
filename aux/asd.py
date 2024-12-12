import os
import json

def Load_Files()->list:
    """
    Toma todos los archivos JSON de la carpeta data y los agrupa en una lista
    """
    output = []
    path_files = os.path.join(os.getcwd(),"data")
    for files in os.listdir(path_files):
        the_file = os.path.join(path_files,files)
        with open(the_file, 'r', encoding='utf-8') as opened:
            texto = json.load(opened)
            if texto["municipality"] == "String/ Nombre del municipio": continue
            output.append(texto)
    return output


