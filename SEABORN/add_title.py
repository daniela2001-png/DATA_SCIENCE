'''
FacetGrids vs. EjesSubplots
En la lección reciente, aprendimos que las funciones de trazado Seaborn crean dos tipos diferentes de objetos: FacetGridobjetos y AxesSubplotobjetos. El método para agregar un título a su trama diferirá según el tipo de objeto que sea.

En el código provisto, hemos utilizado relplot()el conjunto de datos de millas por galón para crear un diagrama de dispersión que muestra la relación entre el peso de un automóvil y su potencia. Este diagrama de dispersión se asigna al nombre de la variable g. Identifiquemos qué tipo de objeto es.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()
