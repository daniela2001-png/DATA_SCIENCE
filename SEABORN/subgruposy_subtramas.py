'''
Gráfico de barras con subgrupos y subtramas
En este ejercicio, volveremos a nuestro conjunto de datos de encuestas de jóvenes e investigaremos si la proporción de personas a las que les gusta la música tecno ( "Likes Techno") varía según su género ( "Gender") o el lugar donde viven ( "Village - town"). ¡Este ejercicio nos dará la oportunidad de practicar las muchas cosas que hemos aprendido a lo largo de este curso!

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.
'''

# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
      ylabel="% Who Like Techno")

# Show plot
plt.show()
