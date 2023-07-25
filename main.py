import pandas as pd
import requests

def acceso_api(paradero="PA184"):
    """
    Realiza una solicitud a la API de transporte público para obtener información
    sobre los buses próximos a un paradero específico.
    
    Argumentos:
    paradero (str): El código del paradero del cual se desea obtener información. 
                    Por defecto, se utiliza el paradero "PA184".
    
    Retorna:
    pd.DataFrame: Un DataFrame con la información obtenida de la API.
    """
    url = f'https://api.xor.cl/red/bus-stop/{paradero}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df_servicios = df['services'].apply(pd.Series)
    return df_servicios

def get_buses(df_servicios):
    """
    Extrae la información relevante de los buses desde un DataFrame de servicios.
    
    Argumentos:
    df_servicios (pd.DataFrame): El DataFrame con la información de los servicios
                                 obtenida de la API.
    
    Retorna:
    list: Una lista que contiene los datos de los buses encontrados en el paradero.
    """
    buses = list()
    for i in range(len(df_servicios)):
        if df_servicios["buses"][i] != []:
            recorrido = df_servicios["id"][i]
            estado = df_servicios["status_description"][i]
            for bus_info in df_servicios["buses"][i]:
                patente = bus_info["id"]
                distancia = bus_info["meters_distance"]
                min_minimos = bus_info["min_arrival_time"]
                min_maximos = bus_info["max_arrival_time"]
                buses.append([recorrido, estado, patente,
                             distancia, min_minimos, min_maximos])
    return buses

def crear_dataframe_buses(buses):
    """
    Crea un DataFrame a partir de la lista de datos de buses obtenida de la API.
    
    Argumentos:
    buses (list): Una lista con los datos de los buses encontrados en el paradero.
    
    Retorna:
    pd.DataFrame: Un DataFrame organizado con la información de los buses, incluyendo
                  el tiempo promedio de llegada de cada bus.
    """
    df_buses = pd.DataFrame(buses, columns=[
                            "Recorrido", "Estado", "Patente", "Distancia", "Min. Mínimos", "Min. Máximos"])
    df_buses["promedio min"] = (
        df_buses["Min. Mínimos"] + df_buses["Min. Máximos"]) / 2
    df_buses["promedio min"] = df_buses["promedio min"].astype(int)
    df_buses = df_buses.sort_values(by=["Distancia"], ascending=False)
    return df_buses

def descargar_csv(df_buses):
    """
    Guarda el DataFrame de buses en un archivo CSV llamado "buses.csv".
    
    Argumentos:
    df_buses (pd.DataFrame): El DataFrame con la información de los buses.
    """
    df_buses.to_csv("buses.csv", index=False, sep=",", encoding="utf-8")

# Ejecución del código
paradero = input("Ingrese el paradero: ")
df_servicios = acceso_api(paradero)
buses = get_buses(df_servicios)
df_buses = crear_dataframe_buses(buses)
descargar_csv(df_buses)
