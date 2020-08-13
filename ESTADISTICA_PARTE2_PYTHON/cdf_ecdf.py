import numpy as np
import matplotlib.pyplot as plt
import ecdf
import seaborn as sns
import pandas as pd

'''
NOTA IMPORTANTE: El CDF empírico se construye a partir de un conjunto de datos reales (en el gráfico a continuación, utilicé 100 muestras de una distribución normal estándar).
El CDF es una construcción teórica; es lo que vería si pudiera tomar una cantidad infinita de muestras.

El CDF empírico generalmente se aproxima bastante bien al CDF, especialmente para muestras grandes
(de hecho, existen teoremas sobre la rapidez con la que converge al CDF a medida que aumenta el tamaño de la muestra).

'''
'''
¿Los datos siguen nuestra historia?
Ha modelado juegos sin hits utilizando una distribución exponencial. Cree un ECDF de los datos reales. Superponga el CDF teórico con el ECDF de los datos. Esto le ayuda a verificar que la distribución exponencial describe los datos observados.
Puede ser útil para recordar la función que ha creado en el curso anterior para calcular la ECDF, así como el código que escribió a trazar lo .

Instrucciones

Calcule un ECDF a partir del tiempo real entre partidos sin hits ( nohitter_times). Utilice la ecdf()función que escribió en el curso de precuela.
Cree un CDF a partir de las muestras teóricas que tomó en el último ejercicio ( inter_nohitter_time).
Trazar x_theory y_theorcomo una línea usando plt.plot(). Luego superponga el ECDF de los datos reales xy ycomo puntos. Para hacer esto, debe especificar los argumentos de la palabra clave marker = '.'y linestyle = 'none'además xy ydentro plt.plot().
Establezca un margen del 2% en el gráfico.
Muestre la trama.

clave:
Para calcular el ECDF de nohitter_times, páselo como argumento a la ecdf()función.
Para crear el CDF a partir de las muestras teóricas, use la ecdf()función una vez más, pasando la matriz de las muestras que tomó en el ejercicio anterior ( inter_nohitter_time).
Para trazar el CDF como una línea, pase x_theory y_theorcomo argumentos a plt.plot(). Para superponer los datos reales como puntos, utilizar plt.plot()con los argumentos x, y, marker = '.'y linestyle = 'none'.
Puede establecer márgenes pasando el margen deseado como argumento a plt.margins().
Para mostrar el gráfico, use plt.show().

'''
# simulacion de matriz de la cantidad de juegos hechos cuando no se hacen ningún hit!
a = np.random.randint(1000, size=(20,20))
print(a)
print('-' * 50)
#sacamos una muestra de cien mil datos con tau que sera nuestar variable poisson
#tau contiene el tiempo por cada juego sin hits == a
tau = np.median(a)
tiempos_entre_partidos_sin_hits = np.random.exponential(tau, 100000)
# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor, label='CDF TEÓRICO')
plt.plot(x, y, marker='.', linestyle='none', label='CDF REAL')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')
plt.legend()
# Show the plot
plt.show()
