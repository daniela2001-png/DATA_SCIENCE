'''
Cambio de estilo y paleta
Volvamos a nuestro conjunto de datos que contiene los resultados de una encuesta realizada a los jóvenes sobre sus hábitos y preferencias. Hemos proporcionado el código para crear un diagrama de conteo de sus respuestas a la pregunta "¿Con qué frecuencia escuchas los consejos de tus padres?". Ahora cambiemos el estilo y la paleta para que esta trama sea más fácil de interpretar.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.
'''

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()


'''
es poco factible pero pondre todos los estilos en seaborn:aqui
Cambiando la escala
En este ejercicio, continuaremos analizando el conjunto de datos que contiene las respuestas de una encuesta de jóvenes. ¿El porcentaje de personas que informan que se sienten solas varía según cuántos hermanos tienen? Averigüemos usando un diagrama de barras, mientras exploramos también las cuatro escalas de diagrama diferentes de Seaborn ("contextos").

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

