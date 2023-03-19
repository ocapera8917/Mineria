import pandas as pd
#url = "https://raw.githubusercontent.com/ocapera8917/Mineria/main/Captura_por_delito_sin_limpieza.csv"
url = "G:\mineria\Proyecto\delitos_sexuales_sin_limpieza.csv"
df  =  pd.read_csv(url)
#df.loc[df['PAIS'].isna() , 'PAIS'] = 'COLOMBIA'
#df['PAIS'] = pd.to_(df['FECHA'])
#df.to_csv('G:\mineria\Proyecto\delitos_sexuales_sin_limpieza.csv', index=False)
print(df.dtypes)
#print(df.isna().sum())
