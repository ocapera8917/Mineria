import pandas as pd
import re
#url = "https://raw.githubusercontent.com/ocapera8917/Mineria/main/Captura_por_delito_sin_limpieza.csv"
url = "G:\mineria\Proyecto\Reporte__Delitos_sexuales_Polic_sin_limpieza.csv"
df  =  pd.read_csv(url)
#df.loc[df['PAIS'].isna() , 'PAIS'] = 'COLOMBIA'
#df['FECHA HECHO'] = pd.to_datetime(df['FECHA HECHO'])
#df['DELITO'] = df['DELITO'].astype(str)
#df.to_csv('G:\mineria\Proyecto\Reporte__Delitos_sexuales_Polic_sin_limpieza.csv', index=False)
#print(df.dtypes)
#print(df)
#url = "G:\mineria\Proyecto\Captura_por_delito_sin_limpieza.csv"
#url="https://raw.githubusercontent.com/luisaarciniegas/auto/main/juegos2.csv"
#df.dtypes
#df['FECHA'] = pd.to_datetime(df['FECHA'])
#df.to_csv('G:\mineria\Proyecto\Captura_por_delito_sin_limpieza.csv', index=False)
#print(df.dtypes)
print(df.isna().sum())
