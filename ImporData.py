import pandas as pd
#url = "https://raw.githubusercontent.com/ocapera8917/Mineria/main/Captura_por_delito_sin_limpieza.csv"
url = "G:\mineria\Proyecto\Captura_por_delito_sin_limpieza.csv"
df  =  pd.read_csv(url)
print(df.isna().sum())
