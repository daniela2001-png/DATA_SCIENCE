'''
Trazar subgrupos en trazados lineales
Continuemos mirando el mpgconjunto de datos. Hemos visto que el promedio de millas por galón para automóviles ha aumentado con el tiempo, pero ¿cómo ha cambiado la potencia promedio de los automóviles con el tiempo? ¿Y esta tendencia difiere según el país de origen?

'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", style='origin',  
            ci=None, markers=True, 
            hue="origin", dashes=False)

# Show plot
plt.show()
