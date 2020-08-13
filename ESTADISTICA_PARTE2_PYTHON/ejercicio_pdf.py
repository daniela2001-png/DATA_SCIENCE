import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''
¿Con qué frecuencia tenemos juegos sin hits?
El número de juegos jugados entre cada juego sin hits en la era moderna (1901-2015) de Major League Baseball se almacena en la matriz nohitter_times.
Si asume que los juegos sin hits se describen como un proceso de Poisson, entonces el tiempo entre los juegos sin hits se distribuye exponencialmente. Como ha visto, la distribución exponencial tiene un solo parámetro, que llamaremos \ (\ tau \), el intervalo de tiempo típico. El valor del parámetro \ (\ tau \) que hace que la distribución exponencial coincida mejor con los datos es el tiempo de intervalo medio (donde el tiempo está en unidades de número de juegos) entre partidos sin hits.
Calcule el valor de este parámetro a partir de los datos. Luego, usa np.random.exponential()para "repetir" la historia de las Grandes Ligas dibujando tiempos entre partidos sin hits a partir de una distribución exponencial con el \ (\ tau \) que encontraste y traza el histograma como una aproximación al PDF.
NumPy, pandas, matlotlib.pyplot y Seaborn han sido importados para usted como np, pd, plt, y sns, respectivamente.

Instrucciones

Siembra el generador de números aleatorios con 42.
Calcule el tiempo medio (en unidades de número de juegos) entre partidos sin hits.
Saque 100.000 muestras de una distribución exponencial con el parámetro que calculó a partir de la media de los tiempos entre partidos sin hits.
Trace el PDF teórico usando plt.hist(). Recuerde que debe utilizar argumentos de palabra clave bins=50, normed=Truey histtype='step'. Asegúrese de etiquetar sus ejes.
Muestra tu trama.

clave:

Puede usar la random.seed()función de NumPy para sembrar el generador de números aleatorios con 42.
Para calcular el tiempo medio, use la meanfunción de Numpy ( np.mean()), pasando la matriz nohitter_timescomo argumento.
Úselo np.random.exponential()para extraer muestras de una distribución exponencial. El primer argumento de la función debe ser el parámetro tauque calculó anteriormente, mientras que el segundo argumento debe ser el tamaño de muestra deseado.
Úselo plt.hist()con los argumentos de palabras clave mencionados en las instrucciones. ¡Asegúrese de estar atento a los errores tipográficos!
Para mostrar su gráfico, use plt.show().

'''
# simulacion de matriz de la cantidad de juegos hechos cuando no se hacen ningún hit!
a = np.random.randint(1000, size=(20,20))
print(a)
print('-' * 50)
#Calculamos el tiempo medio (en unidades de número de juegos) entre partidos sin hits.
tau = np.mean(a)
print(tau)
print('-' * 50)
#Saque 100.000 muestras de una distribución exponencial con el parámetro que calculó a partir de la media de los tiempos entre partidos sin hits.
tiempos_entre_partidos_sin_hits = np.random.exponential(tau, 100000)
print(tiempos_entre_partidos_sin_hits)
# Plot the PDF and label axes
plt.style.use('bmh')
_ = plt.hist(tiempos_entre_partidos_sin_hits, bins=50, histtype='step', alpha=0.8, density=True)
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')
_ = plt.annotate('Vemos la forma típica de la distribución exponencial, yendo desde un máximo en 0 y decayendo hacia la derecha', xy=(1000, 0.0010))

# Show the plot
plt.show()
