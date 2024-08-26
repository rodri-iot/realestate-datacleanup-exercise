import pandas as pd

#Ejercicio 0
ds = pd.read_csv('assets/real_estate.csv', sep=';')
#print(ds.columns.tolist())
#El siguiente print sirve para verificar el nombre de las columnas
#print(ds.columns.tolist())

#Ejercicio 1
"""
max_price = ds['price'].max()
max_house = ds[ds['price'] == max_price]
print(f"La casa con dirección en {max_house['address'].values[0]} es la más cara y su precio es de {max_house['price'].values[0]} USD")
"""

#Ejercicio 2
"""
min_price = ds['price'].argmin()
min_house = ds['price'].min()
print(f"La casa con dirección en {min_price} es la más barata y su precio es de {min_house} USD")
"""

#Ejercicio 3
"""
max_sqm = ds['surface'].max()
big_house = ds[ds['surface'] == max_sqm]
print(f"La casa más grande está ubicada en {big_house['address'].values[0]} y su superficie es de {big_house['surface'].values[0]} metros")

min_sqm = ds['surface'].min()
small_house = ds[ds['surface'] == min_sqm]
print(f"La casa más pequeña está ubicada en {small_house['address'].values[0]} y su superficie es de {small_house['surface'].values[0]} metros")
"""

#Ejercicio 4
"""
populations = ds['level5'].unique()
print(', '.join(populations))
"""

#Ejercicio 5
"""
print(ds.isna())
"""

#Ejercicio 06
"""
values_nas = ds.dropna(axis=1, how="any", inplace=True)
print(ds.isna())
"""

#Ejercicio 07
"""
columna_5 = ds[ds['level5'] == "Arroyomolinos (Madrid)"]
price_mean = columna_5['price'].mean()
print(price_mean)
print(columna_5)
"""

#Ejercicio 08
"""
import matplotlib.pyplot as plt

arroyomolinos_data = ds[ds['level5'] == "Arroyomolinos (Madrid)"]
plt.hist(arroyomolinos_data['price'], bins=20, edgecolor='red')
plt.xlabel("Precio")
plt.ylabel("Frrecuencia")
plt.show()
"""

#Ejercicio 09
"""
price_valdemorillo = ds[ds['level5'] == 'Valdemorillo']
price_galapagar = ds[ds['level5'] == 'Galapagar']
mean_price_v = price_galapagar['price'].mean()
mean_price_g = price_valdemorillo['price'].mean()
print(f"El precio promedio de Valdemorillo ese {mean_price_v} y el precio promedio de Galapagar es {mean_price_g}, no son iguales.")
"""

#Ejercicio 10
"""
avg = ds[ds['level5'].isin(["Valdemorillo", "Galapagar"])]
ds['pps'] = avg['price']/avg['surface']

avg_v = ds[ds['level5']=='Valdemorillo']['pps'].mean()
avg_g = ds[ds['level5']=='Galapagar']['pps'].mean()

print(f"No son los mismos precios por metro cuadrado. El promedio de Valdemorillo es {avg_v} y el de Galapagar es {avg_g}")
"""

#Ejercicio 11
"""
import matplotlib.pyplot as plt

plt.scatter(ds['surface'], ds['price'])

plt.title('Relación entre superficie y precio de las casas')
plt.xlabel('Supeerficie m2')
plt.ylabel('Precio')
plt.show()
print('La relación entre la superficie y el precio de las casas es positiva, lo que sugiere que las casas más grandes y espaciosas tienen un precio más elevado, esto es lógico')
"""

#Ejercicio 12
"""
num_agencies = ds['id_realEstates'].nunique()
print(f'El número de agencias son: {num_agencies}')
"""

#Ejercicio 13
"""
poblacion_casa = ds['level5'].value_counts()
poblacion_mas_casas = poblacion_casa.index[0]
num_casas = poblacion_casa.iloc[0]

print(f"La población con más casas es {poblacion_mas_casas} y el númeror de casas es {num_casas}")
"""

#Ejercicio 14
"""
cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]
print(cinturon_sur)
"""

#Ejercicio 15
"""
import matplotlib.pyplot as plt
cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]

mediana_precios = cinturon_sur.groupby('level5')['price'].median()

plt.bar(x=mediana_precios.index, height=mediana_precios.values)

plt.title('Mediana de los precios en el cinturon sur')
plt.xlabel('Ciudad')
plt.ylabel('Mediana precios')
plt.show()

"""

#Ejercicio 16
"""
cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]

media_precio = cinturon_sur['price'].mean() 
varianza_precio = cinturon_sur['price'].var()

media_habitaciones = cinturon_sur['rooms'].mean()
varianza_habitaciones = cinturon_sur['rooms'].var()

media_superficie = cinturon_sur['surface'].mean()
varianza_superficie = cinturon_sur['surface'].var()

media_banos = cinturon_sur['bathrooms'].mean()
varianza_banos = cinturon_sur['bathrooms'].var()

print(f"Precio - Media: {media_precio} Varianza: {varianza_precio}")
print(f"Habitaciones - Media: {media_habitaciones} Varianza: {varianza_habitaciones}")
print(f"Superficie - Media: {media_superficie} Varianza: {varianza_superficie}")
print(f"Baños - Media: {media_banos} Varianza: {varianza_banos}")
"""

#Ejercicio 17
"""
cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]

casas_mas_caras = cinturon_sur.loc[cinturon_sur.groupby('level5')['price'].idxmax()]
print(casas_mas_caras[['level5', 'address', 'price']])
"""

#Ejercicio 18
"""
import matplotlib.pyplot as plt

cinturon_sur = ds[ds['level5'].isin(["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"])] 

plt.figure(figsize=(12, 6))

for i, level in enumerate(cinturon_sur['level5'].unique()):
    data = cinturon_sur[cinturon_sur['level5'] == level]['price']
    plt.hist(data, alpha=0.5, label=level, bins=20)

plt.title('Histogramas de precios normalizados por población')
plt.xlabel("Precio normalizado")
plt.ylabel('Frecuencia')
plt.legend(title='Población')
plt.show()
"""

#Ejercicio 19
"""
import pandas as pd
ds = pd.read_csv('assets/real_estate.csv', sep=';')

avg = ds[ds['level5'].isin(["Getafe", "Alcorcón"])]
ds['pps'] = avg['price']/avg['surface']

avg_g = ds[ds['level5']=='Getafe']['pps'].mean()
avg_a = ds[ds['level5']=='Alcorcón']['pps'].mean()

if avg_g > avg_a:
    print("En Getafe el precio por metro cuadrado es mayor que en Alcorcón")
elif avg_g < avg_a:
    print("En Alcorcón el precio por metro cuadrado es mayor que en Getafe")
else:
    print("En Alcorcón y en Getafe los precios por metro cuadrado son iguales")
"""

#Ejercicio 20
"""
import matplotlib.pyplot as plt

cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
poblaciones = cinturon_sur['level5'].unique()
colors = ['b', 'g', 'r', 'c']
for i, poblaciones in enumerate(poblaciones):
    row = i//2
    col = i%2
    axs[row,col].scatter(cinturon_sur[cinturon_sur['level5'] == poblaciones]['rooms'], cinturon_sur[cinturon_sur['level5'] == poblaciones]['price'], color=colors[i])
    axs[row,col].set_title(f"Poblacion: {poblaciones}")
    axs[row,col].set_xlabel('Habitaciones')
    axs[row,col].set_ylabel('Precios')
plt.tight_layout()
plt.show()
"""

#Ejercicio 21
#"""
from ipyleaflet import Map, basemaps, CircleMarker

map = Map(center = (40.4168, -3.7038), zoom = 10, min_zoom = 1, max_zoom = 20, basemap=basemaps.OpenStreetMap.Mapnik)

cinturon_sur = ds[ds['level5'].isin(['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón'])]
poblaciones = cinturon_sur['level5'].unique()

for poblacion in cinturon_sur['level5'].unique():
    coords = cinturon_sur[cinturon_sur['level5'] == poblacion][['latitude', 'longitude']].values
    for coord in coords:
        circle = CircleMarker(location=(coord[0], coord[1]), radius=50, 
                              color='blue' if poblacion == 'Fuenlabrada' else 
                              'green' if poblacion == 'Leganés' else 
                              'red' if poblacion == 'Getafe' else 'orange')
        map.add_layer(circle)

map
#"""