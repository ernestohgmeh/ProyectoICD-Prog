import os
import json
import matplotlib.pyplot as mplp


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

def Get_Fixed_Objets()->list:
    """
    Des-anida la informacion dentro de "info" y devuelve una lista
    """
    raw_files = Load_Files()
    temp = []
    for k in raw_files:
        cosa = {"municipality": k["municipality"]}
        cosa.update(k["info"])
        temp.append(cosa)
    return temp

def Id_Show(lista:list):
    """
    Devuelve el nombre y la posicion en la lista para q el usuario pueda acceder a su informacion
    """
    id = []
    for k, i in enumerate(lista):
        id.append(f"{k}- {i["nameLocal"]}")
    for i in id:
        print(f"{i}")
        
        
def Graf_Bar(id:int,temp = Get_Fixed_Objets()):
    """
    grafico q muestre los precios de los productos de una misma clasif
    """
    graf_output = []

    for k in temp[id]["menu"]["platoFuerte"]:
        if k["clasificacion"].lower() == "carne roja": graf_output.append((k["foodName"],k["foodPrecio"])) #importante normalizar la clasf hasta q se arregle

    nombre_producto = []
    precio_producto = []
    for k in graf_output:
        nombre_producto.append(k[0])
        precio_producto.append(k[1])

    mplp.bar(nombre_producto,precio_producto,color='#721121')
    mplp.xlabel('Nombre del Producto')
    mplp.ylabel('Precio')
    mplp.title('Precio de las carnes rojas del ' + temp[id]["nameLocal"])
    mplp.xticks(rotation=90, fontsize= 7)
    mplp.legend("oal")
    mplp.show()
