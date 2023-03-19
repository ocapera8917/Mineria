import pandas as pd

#url="https://raw.githubusercontent.com/luisaarciniegas/auto/main/juegos2.csv"
#url = "https://raw.githubusercontent.com/ocapera8917/Mineria/main/Captura_por_delito_sin_limpieza.csv"
url = "G:\mineria\Proyecto\Captura_por_delito_sin_limpieza.csv"
df  =  pd.read_csv(url)
#df.dtypes
df['FECHA'] = pd.to_datetime(df['FECHA'])
df.to_csv('G:\mineria\Proyecto\Captura_por_delito_sin_limpieza.csv', index=False)
print(df.dtypes)