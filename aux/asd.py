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


def Promedio_recortado_seccion(lista:list):
    """
    Toma los precios de los productos, los ordena y devuelve el promedios sin contar el 10% inferior y superior
    """
    
    porciento = int(len(lista) * 0.1)
    if len(lista) == 0: return 0
    lista.sort(key=lambda x: x["foodPrecio"])
    while porciento > 0:
        lista.pop(0)
        lista.pop(-1)
        porciento -= 1
    
    output = 0
    for k in lista:
            output += int(k["foodPrecio"])
    output /= len(lista)
    return output

def Promedio_restaurant(dicc:dict):
    """
    devuelve promedio recortado por seccion de todas las secciones y cuanto gasta una persona
    """
    
    entrante = dicc["menu"]["entrantes"] = Promedio_recortado_seccion(dicc["menu"]["entrantes"])
    fuerte = dicc["menu"]["platoFuerte"] = Promedio_recortado_seccion(dicc["menu"]["platoFuerte"])
    postres = dicc["menu"]["postre"] = Promedio_recortado_seccion(dicc["menu"]["postre"])
    bebidas = dicc["menu"]["bebidas"] = Promedio_recortado_seccion(dicc["menu"]["bebidas"])
    
    return (entrante + fuerte + postres + bebidas*2) / 5
    
    

def Promedio_municipio(lista:list):
    """
    Toma los promedios de los restaurantes y devuelve el promedios
    """
    salida = [{"Cerro": []},{"Centro": []},{"Vieja": []},{"Plaza": []},{"Playa": []},{"Este": []},{"Gua": []},{"Diez": []},{"Boyeros": []},{"Cotorro": []},{"Arroyo": []},{"San": []},{"Marianao": []},{"Regla": []},{"Lisa": []}]
    for k in lista:
        if k["municipality"].lower() == "cerro": salida[0]["Cerro"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "centro habana": salida[1]["Centro"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "habana vieja": salida[2]["Vieja"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "plaza de la revolucion": salida[3]["Plaza"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "playa": salida[4]["Playa"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "habana del este": salida[5]["Este"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "guanabacoa": salida[6]["Gua"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "10 de octubre": salida[7]["Diez"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "boyeros": salida[8]["Boyeros"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "cotorro": salida[9]["Cotorro"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "arroyo naranjo": salida[10]["Arroyo"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "san miguel del padron": salida[11]["San"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "marianao": salida[12]["Marianao"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "regla": salida[13]["Regla"].append(Promedio_restaurant(k))
        elif k["municipality"].lower() == "lisa": salida[14]["Lisa"].append(Promedio_restaurant(k))
    
    
    for k in salida:
        for key in k.items():
            if len(k[key[0]]) == 0: k[key[0]] = 0
            else: k[key[0]] = sum(k[key[0]]) / len(k[key[0]])
    return salida
            