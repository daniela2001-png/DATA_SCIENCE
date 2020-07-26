'''

Visualización de desviación estándar con gráficos de líneas
En el último ejercicio, observamos cómo las millas promedio por galón logradas por los automóviles han cambiado con el tiempo. Ahora usemos un diagrama lineal para visualizar cómo la distribución de millas por galón ha cambiado con el tiempo.

Seaborn ha sido importado como snsy matplotlib.pyplotha sido importado como plt.

'''
import seaborn as sns
import matplotlib.pyplot as plt

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()


'''
Excelente. A diferencia del diagrama en el último ejercicio, este diagrama nos muestra la distribución de millas por galón para todos los autos en cada año
'''
