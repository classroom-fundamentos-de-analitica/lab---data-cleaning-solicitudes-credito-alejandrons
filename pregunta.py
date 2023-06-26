"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.dropna()

    # Estandarizar el formato de las columnas
    df.sexo = df.sexo.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    # Conversión de comuna a dato entero
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    # Estandarizando la columna "idea_negocio"
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-", " ")
    df.idea_negocio = df.idea_negocio.str.replace("_", " ")
    df.idea_negocio = df.idea_negocio.str.strip()

    # Estandarizando la columna "barrio"
    df.barrio = df.barrio.str.replace("-", " ")
    df.barrio = df.barrio.str.replace("_", " ")

    # Estandarización de las fechas
    def correccion(fecha):
        componentes = fecha.split("/")
        if len(fecha[0]) == 4:
            nueva_fecha = "/".join(sorted(componentes,reverse=True))
        else:
            nueva_fecha = fecha
        return nueva_fecha
    
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(correccion)
    
    # Tener todos los datos del monto del crédito en el mismo formato
    df.monto_del_credito = df.monto_del_credito.str.lstrip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.str.replace(" ","")
    df.monto_del_credito = df.monto_del_credito.astype(float)
    
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("-",' ')
    df.línea_credito = df.línea_credito.str.replace("_",' ')

    df = df.drop_duplicates(subset=["sexo","tipo_de_emprendimiento","idea_negocio",
                                    "barrio", "estrato", "comuna_ciudadano",
                                    "fecha_de_beneficio", "monto_del_credito", "línea_credito"])
    

    return df

