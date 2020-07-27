'''
Diagrama de caja con subgrupos
En este ejercicio, veremos el conjunto de datos que contiene las respuestas de una encuesta realizada a los jóvenes. Una de las preguntas formuladas a los jóvenes fue: "¿Te interesa tener mascotas?" Exploremos si la distribución de edades de los que respondieron "sí" tiende a ser mayor o menor que los que respondieron "no", controlando por género.
'''

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue='Interested in Pets')

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Show plot
plt.show()
