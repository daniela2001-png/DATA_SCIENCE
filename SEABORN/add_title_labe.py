'''
Agregar un título y etiquetas de eje
Continuemos mirando el conjunto de datos de millas por galón. Esta vez crearemos un diagrama lineal para responder la pregunta: ¿Cómo cambia el promedio de millas por galón logrado por los automóviles con el tiempo para cada uno de los tres lugares de origen? Para mejorar la legibilidad de este gráfico, agregaremos un título y etiquetas de eje más informativas.

En el código provisto, creamos el diagrama de línea usando la lineplot()función. Tenga en cuenta que lineplot()no admite la creación de subtramas, por lo que devuelve un AxesSubplotobjeto en lugar de un FacetGridobjeto.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels

g.set(xlabel="Car Model Year",
ylabel="Average MPG")

# Show plot
plt.show()
