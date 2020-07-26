'''
Cambiar el estilo de los puntos de trazado de dispersión
Continuemos explorando el mpgconjunto de datos de Seaborn observando la relación entre qué tan rápido puede acelerar un automóvil ( "acceleration") y su eficiencia de combustible ( "mpg"). ¿Estas propiedades varían según el país de origen ( "origin")?

Tenga en cuenta que la "acceleration"variable es el tiempo para acelerar de 0 a 60 millas por hora, en segundos. Los valores más altos indican una aceleración más lenta.

'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', hue='origin', style='origin')



# Show plot
plt.show()


'''
OBSERVACION D ELA TRAMA:Los automóviles de los EE. UU. Tienden a acelerar más rápidamente y a obtener menos millas por galón en comparación con los automóviles de Europa y Japón.
'''
