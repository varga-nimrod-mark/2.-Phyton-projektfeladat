import pandas as panda
import numpy as nump
import matplotlib.pyplot as graf
import os

mappa = os.path.dirname(__file__)
fajl_utvonal = os.path.join(mappa, 'air_quality_dataset.csv')

matrix = panda.read_csv(fajl_utvonal)
matrix.columns = matrix.columns.str.strip()

aqi_oszlop = 'AQI' if 'AQI' in matrix.columns else 'PM2.5'

print("Adatok beolvasva! Sorok száma:", len(matrix))
print()


# 1

matrix['PM_Arany'] = matrix['PM2.5'] / matrix['PM10']
matrix['pm2.5/pm10 arány'] = panda.qcut(matrix[aqi_oszlop], 4, labels=['Alacsony', 'Mérsékelt', 'Magas', 'Kritikus'])
valasz1 = matrix.groupby('pm2.5/pm10 arány', observed=False)['PM_Arany'].mean()

print("1. vizsgált szempont")
print(valasz1.to_string())
print()

# 2,
atlag = nump.mean(matrix['PM2.5'])
szoras = nump.std(matrix['PM2.5'])
matrix['Z_score'] = (matrix['PM2.5'] - atlag) / szoras
anomaliak = matrix[(matrix['Z_score'] > 3) | (matrix['Z_score'] < -3)]

print("2.vizsgált szempont")
print("Átlag:", round(atlag, 2))
print("Szórás:", round(szoras, 2))
print("Anomáliák száma:", len(anomaliak))
print()

# 3.

matrix['PM_30_napos'] = matrix['PM2.5'].rolling(30, min_periods=1).mean()
matrix['PM_360_napos'] = matrix['PM2.5'].rolling(360, min_periods=1).mean()

print("3.vizsgált szempont")
print("30 napos gördülő átlag közepe:", round(matrix['PM_30_napos'].mean(), 2))
print("1 éves gördülő átlag közepe:", round(matrix['PM_360_napos'].mean(), 2))
print()


# 4

eredeti_atlag = matrix['PM2.5'].mean()
eredeti_szoras = matrix['PM2.5'].std()

median_ertek = matrix['PM2.5'].median()
matrix['PM_imputed'] = matrix['PM2.5'].fillna(median_ertek)

uj_atlag = matrix['PM_imputed'].mean()
uj_szoras = matrix['PM_imputed'].std()

print("4.vizsgált szempont")
print("Eredeti átlag és szórás:", round(eredeti_atlag, 2), round(eredeti_szoras, 2))
print("Új átlag és szórás:", round(uj_atlag, 2), round(uj_szoras, 2))
print()
# 5.
szennyezoek_atlag = matrix[['PM2.5', 'PM10', 'NOx', 'NO2', 'SO2']].mean()

print("5.vizsgált szempont")
print(szennyezoek_atlag.to_string())
print()

# grafikon csinálás

graf.figure(figsize=(15, 8))

# 1. Grafikon
graf.subplot(2, 3, 1)
valasz1.plot(kind='bar', color='blue',edgecolor='black')
graf.title('PM2.5/PM10 arány')
graf.xlabel('Szenyezetség mértéke')
graf.ylabel('Arány')

# 2. Grafikon
graf.subplot(2, 3, 2)
graf.hist(matrix['Z_score'], bins=25, color='green', edgecolor='black')
graf.title('Kiugró értékek')


# 3. Grafikon
graf.subplot(2, 3, 3)
graf.plot(matrix['PM2.5'], color='gray', alpha=0.4, label='Napi')
graf.plot(matrix['PM_30_napos'], color='red', label='30 napos')
graf.plot(matrix['PM_360_napos'], color='blue', label='1 éves')
graf.title('Rövid és hosszú távú levegőminőség')
graf.legend()


# 4. Grafikon
graf.subplot(2, 3, 4)
graf.hist(matrix['PM2.5'].dropna(), bins=20, color='orange', alpha=0.6, edgecolor='black')
graf.hist(matrix['PM_imputed'], bins=20, color='blue', alpha=0.6,edgecolor='black', label='Generált')
graf.title('Hibás adatok feltöltése')
graf.xlabel('PM2.5 érték')
graf.legend()

# 5. Grafikon
graf.subplot(2, 3, 5)
graf.pie(
    szennyezoek_atlag, 
    labels=szennyezoek_atlag.index, 
    autopct='%1.1f%%', 
    colors=['skyblue', 'lightgreen', 'orange', 'salmon', 'violet']
)
graf.title('5. Kérdés: Szennyezők aránya')
graf.show()