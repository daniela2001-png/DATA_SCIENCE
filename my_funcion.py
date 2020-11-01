#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
dataframe = [{
    'marca': 'koaj',
    'precio_camisa':80000,
    'precio_pantalon':100000
},
    {
    'marca': 'zara',
    'precio_camisa':100000,
    'precio_pantalon':200000
    }]
df =pd.DataFrame(dataframe)
print(df)
fig, ax = plt.subplots()
ax.plot(df['marca'], df['precio_camisa'], marker='o', label='camisas', linestyle="--")
ax.plot(df['marca'], df['precio_pantalon'], marker='o', label='pantalones', linestyle="--")

plt.xlabel('marcas de ropa')
plt.ylabel('precios')
plt.legend()
plt.show()

def funcion(*args, tienda='tienda de barrio'):
    var = []
    for i in args:
        var.append(i)
        tiendas = ['zara', 'koaj']
        if (i == 'camisa') and args[-1] == 'koaj':
            precio_camisa = 20.000
            print('el precio de la camisa marca {} es: {}'.format(args[-1], precio_camisa))
        if (i == 'pantalon') and args[-1] == 'koaj':
            precio_pantalon = 80.000
            print('el precio del pantalon marca {} es: {}'.format(args[-1], precio_pantalon))
        if (i == 'camisa') and args[-1] == 'zara':
            precio_camisa = 50.000
            print('el precio de la camisa marca {} es: {}'.format(args[-1], precio_camisa))
        if (i == 'pantalon') and args[-1] == 'zara':
            precio_pantalon = 200.000
            print('el precio del pantalon marca {} es: {}'.format(args[-1], precio_pantalon))
    #print(var)

funcion('pantalon', 'camisa', 'zara')
