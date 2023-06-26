"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace=True)

    # Estandarizar el formato de las columnas de texto

    for col in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
        df[col] = df[col].str.lower()
        df[col] = df[col].apply(lambda i: i.replace('-',' '))
        df[col] = df[col].apply(lambda i: i.replace('_',' '))
    
    # Conversión de comuna a dato entero
    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)
    
    
    # Estandarización de las fechas
    def correccion(fecha):
        componentes = fecha.split('/')
        if len(componentes[0]) == 4:
            nueva_fecha = '/'.join(reversed(componentes))
        else:
            nueva_fecha = fecha
        return nueva_fecha
    
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(correccion)
    
    # Tener todos los datos del monto del crédito en el mismo formato
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.str.replace(' ','')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(subset=["sexo","tipo_de_emprendimiento","idea_negocio",
                                    "barrio", "estrato", "comuna_ciudadano",
                                    "fecha_de_beneficio", "monto_del_credito",
                                    "línea_credito"],
                                    inplace=True)
    

    return df