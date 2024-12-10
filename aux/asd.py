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
            if opened["minicipality"] == "String/ Nombre del municipio": continue
            texto = json.load(opened)
            output.append(texto)
    return output


