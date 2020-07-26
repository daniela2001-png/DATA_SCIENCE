'''

Interpretar diagramas de líneas
En este ejercicio, continuaremos explorando el mpgconjunto de datos de Seaborn , que contiene una fila por modelo de automóvil e incluye información como el año en que se fabricó el automóvil, su eficiencia de combustible (medido en "millas por galón" o "MPG") y su país de origen (EE. UU., Europa o Japón).

¿Cómo ha cambiado con el tiempo el promedio de millas por galón logradas por estos autos? ¡Usemos gráficos de líneas para descubrirlo!

'''

# Import Matplotlib and Seaborn
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        # Create line plot
        sns.relplot(x='model_year', y='mpg', data=mpg, kind='line')
        
        
        # Show plot
        plt.show()

'''
NOTA IMPORTANTE:  La región sombreada representa un intervalo de confianza para la media, no la distribución de las observaciones.
'''
