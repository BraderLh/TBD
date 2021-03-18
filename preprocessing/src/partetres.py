import csv

import pandas as pd
import os
import shutil
import glob
input_folder = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Laboratorio\Tarea2\weka\preprocessing\input'
output_folder = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Laboratorio\Tarea2\weka\preprocessing\output'

input_folder_tbd = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Práctica\Proyecto Final\dataset'
output_folder_tbd = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE C\Tópicos en BD\Práctica\Proyecto Final\dataset\output'


in_products = input_folder + '\products.csv'
in_catalog = input_folder + '\catalogorders.csv'
in_web = input_folder + '\weborders.csv'

out_products = output_folder + '\productscleaned.csv'
out_catalog = output_folder + '\catalogcleaned.csv'
out_web = output_folder + '\webcleaned.csv'
out_final = output_folder + "\datasetfinal.csv"
out_final_cleaned = output_folder + "\integracion" + '\datasetfinalclened.csv'
out_weka_final = output_folder + '\integracion' + '\wekafinal.csv'

in_dataset_tbd = input_folder_tbd + '\indicadoresrural2018.csv'
out_dataset_tbd = output_folder_tbd + '\indicadoresrural2018.csv'


def save_data_folder(origin, destiny):
    for root, dirs, files in os.walk(origin):
        for file in files:
            if file.endswith(".csv"):
                shutil.copy2(os.path.join(root, file), destiny)


def opencsv(file):
    df = pd.read_csv(file, sep=";", engine='python')
    print("Cantida de Filas: ", df.shape[0])
    print("Cantidad de Columnas: ", df.shape[1])
    print("Información del archivo:\n", df.info())
    print("Campos faltantes por cada columna:\n", df.isnull().sum())
    #print("Datos faltantes en todo el dataset:\n", df.isna())
    print("Existe algun valor nulo o vacío: ", df.isna().values.any())


def preprocessing(in_file, output_file):
    copycsv = pd.read_csv(in_file, sep=";", engine='python')
    copycsv.to_csv(output_file, index=False, sep=';')
    pp = pd.read_csv(output_file, sep=';', engine='python')
    """CATALOG ORDERS"""
    #print(pp['CATALOG'])
    #pp['CATALOG'].fillna('Empty', inplace=True)
    #print(pp['QTY'].isnull())
    #pp['QTY'].fillna(0, inplace=True)


    """WEB ORDERS"""
    #print(pp['QTY'])
    #pp['QTY'].fillna(0, inplace=True)


    """QUITAR FILAS"""
    pp.dropna(axis=0,inplace=True)
    #print(pp["QTY"].fillna(0, inplace=True))

    pp = pp.replace(0)

    """Guarda el archivo limpiado sin comas"""
    pp.to_csv(output_file, sep=';', index=False)


def joincsv(indir, out_folder):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    listdf = []
    for filename in fileList:
        df = pd.read_csv(filename, sep=";", engine='python')
        listdf.append(df)
        print(filename)

    listdf[0].columns = ['ID_CAT', 'INV_CAT', 'DATE_CAT', 'CATALOG', 'PCODE_CAT', 'QTY_CAT', 'CUSTNUM_CAT']
    #listdf[0] = listdf[0].set_index('PCODE_CAT')
    listdf[1].columns = ['ID_PRO', 'TYPE', 'DESCRIP', 'PRICE', 'COST', 'PCODE_PRO', 'SUPPLIER']
    #listdf[1] = listdf[1].set_index('PCODE_PRO')
    listdf[2].columns = ['ID_WEB', 'INV_WEB', 'PCODE_WEB', 'DATE_WEB', 'CATALOG', 'QTY_WEB', 'CUSTUM_WEB']
    #listdf[2] = listdf[2].set_index('PCODE_WEB')
    print(listdf[0].columns)
    print("Catalog csv: ", listdf[0].shape)
    print(listdf[1].columns)
    print("Products csv: ", listdf[1].shape)
    print(listdf[2].columns)
    print("Web csv:", listdf[2].shape)
    #print(listdf[0].head())
    #print(listdf[1].head())
    #print(listdf[2].head())
    join = pd.merge(listdf[0], listdf[2], left_on='PCODE_CAT', right_on='PCODE_WEB', how='outer')
    print(join.columns)
    print(join.head(3))
    print(join.shape)
    print(join.isnull().sum())
    print(join.tail())
    #print(join.index())
    second_join = pd.merge(join, listdf[1], left_on='PCODE_CAT', right_on='PCODE_PRO', how='outer')
    print(second_join.columns)
    print(second_join.shape)
    print(second_join.isnull().sum())
    second_join.to_csv(out_folder, sep=";", index=False)
    print("Terminado!")
    #print(frame.info())


def weka_aception(file, out_file):
    leer = pd.read_csv(file, sep=';', engine='python')
    leer.to_csv(out_file, sep=',', index=False, quoting=csv.QUOTE_NONE)


def coma_to_ptcoma(file, out_file):
    leer = pd.read_csv(file, sep=',', engine='python')
    leer.to_csv(out_file, sep=';', index=False, quoting=csv.QUOTE_NONE)
    print("completed!")


opencsv(out_dataset_tbd)
#preprocessing(in_web, out_web)
#opencsv(out_web)
"""opencsv(in_web)
preprocessing(in_web, out_web)
opencsv(out_web)"""
#opencsv(out_web)
#opencsv(out_catalog)
#opencsv(out_products)
#joincsv(output_folder, out_final)
#preprocessing(out_final, out_final_cleaned)
#opencsv(out_final_cleaned)
#weka_aception(out_final_cleaned, out_weka_final)
#coma_to_ptcoma(in_dataset_tbd, out_dataset_tbd)
