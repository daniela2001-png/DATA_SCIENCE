'''
Etiquetas rotativas x-tick
En este ejercicio, continuaremos observando el conjunto de datos de millas por galón. En el código provisto, creamos un gráfico de puntos que muestra la aceleración promedio de los automóviles en cada uno de los tres lugares de origen. Tenga en cuenta que la "acceleration"variable es el tiempo para acelerar de 0 a 60 millas por hora, en segundos. Los valores más altos indican una aceleración más lenta.

Usemos este gráfico para practicar la rotación de las etiquetas de la marca x. Recuerde que la función para rotar las etiquetas de tick x es una función Matplotlib independiente y no una función aplicada al objeto de trazado en sí.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.


'''

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels

plt.xticks(rotation=90)
# Show plot
plt.show()
