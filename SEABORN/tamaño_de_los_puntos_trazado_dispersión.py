'''
Cambiar el tamaño de los puntos de trazado de dispersión
En este ejercicio, exploraremos el mpgconjunto de datos de Seaborn , que contiene una fila por modelo de automóvil e incluye información como el año en que se fabricó el automóvil, la cantidad de millas por galón ("MPG") que logra, la potencia de su motor ( medido en "caballos de fuerza"), y su país de origen.

¿Cuál es la relación entre la potencia del motor de un automóvil ( "horsepower") y su eficiencia de combustible ( "mpg")? ¿Y cómo varía esta relación según la cantidad de cilindros ( "cylinders") que tiene el automóvil? Vamos a averiguar.

Continuemos usando en relplot()lugar de scatterplot()ya que ofrece más flexibilidad.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders", hue='cylinders')

# Show plot
plt.show()

'''
OBSERVACION DE LA TRAMA: Los automóviles con mayor potencia tienden a obtener una menor cantidad de millas por galón. También tienden a tener un mayor número de cilindros
'''
