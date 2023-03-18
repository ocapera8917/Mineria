import pandas as pd
import csv
import chardet

#url="https://raw.githubusercontent.com/luisaarciniegas/auto/main/juegos2.csv"
#url = "https://raw.githubusercontent.com/ocapera8917/Mineria/main/Bases.csv"
#df=  pd.read_csv(url)
#df.head(5)
with open('G:\mineria\Proyecto\Bases.csv', 'rb') as archivo:
    resultado = chardet.detect(archivo.read())
    codificacion = resultado['encoding']

with open('G:\mineria\Proyecto\Bases.csv', encoding='utf-8-sig') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)

    #decode_data = data.decode('utf-8',errors='ignore')