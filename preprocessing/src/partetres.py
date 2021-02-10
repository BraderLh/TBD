import pandas as pd
import os
import shutil

input_folder = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Laboratorio\Tarea2\weka\preprocessing\input'
output_folder = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Laboratorio\Tarea2\weka\preprocessing\output'

in_products = input_folder + '\products.csv'
in_catalog = input_folder + '\catalogorders.csv'
in_web = input_folder + '\Web_orders2.csv'

out_products = output_folder + '\productscleaned.csv'
out_catalog = output_folder + '\catalogcleaned.csv'
out_web = output_folder + '\webcleaned.csv'


def save_data_folder(origin, destiny):
    for root, dirs, files in os.walk(origin):
        for file in files:
            if file.endswith(".csv"):
                shutil.copy2(os.path.join(root, file), destiny)


def opencsv(file):
    df = pd.read_csv(file, sep=",", engine='python')
    print("Información del archivo:\n", df.info())
    print("Campos faltantes por cada columna:\n", df.isnull().sum())
    print("Datos faltantes en todo el dataset:\n", df.isna())
    print(df.isna().values.any())


def preprocessing(in_file, output_file):
    copycsv = pd.read_csv(in_file, engine='python')
    copycsv.to_csv(output_file, index=False)
    pp = pd.read_csv(output_file, sep=',', engine='python')
    """CATALOG ORDERS"""
    #print(pp['CATALOG'])
    #pp['CATALOG'].fillna('Empty', inplace=True)
    #print(pp['QTY'].isnull())
    #pp['QTY'].fillna(0, inplace=True)


    """WEB ORDERS"""
    print(pp['QTY'])
    pp['QTY'].fillna(0, inplace=True)


    """QUITAR FILAS"""
    #pp.dropna(axis=0, inplace=True)
    #print(pp["QTY"].fillna(0, inplace=True))

    """Guarda el archivo limpiado sin comas"""
    pp.to_csv(output_file, index=False)


#opencsv(in_catalog)
#preprocessing(in_catalog, out_catalog)
#opencsv(out_catalog)
opencsv(in_web)
preprocessing(in_web, out_web)
opencsv(out_web)
