'''

Usando una paleta personalizada
Hasta ahora, hemos analizado varias cosas en el conjunto de datos de las respuestas a las encuestas de los jóvenes, incluido su uso de Internet, la frecuencia con la que escuchan a sus padres y cuántos de ellos informan sentirse solos. Sin embargo, una cosa que no hemos hecho es un resumen básico del tipo de personas que respondieron esta encuesta, incluida su edad y sexo. Proporcionar estos resúmenes básicos siempre es una buena práctica cuando se trata de un conjunto de datos desconocido.

El código proporcionado creará un diagrama de caja que muestra la distribución de edades para los encuestados varones frente a las mujeres. Ajustemos el código para personalizar la apariencia, esta vez usando una paleta de colores personalizada.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(['#39A7D0', '#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

