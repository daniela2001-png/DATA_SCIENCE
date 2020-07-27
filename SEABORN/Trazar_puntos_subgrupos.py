'''

Trazar puntos con subgrupos
Continuemos explorando el conjunto de datos de estudiantes en la escuela secundaria. Esta vez, haremos la pregunta: ¿estar en una relación romántica asociada con una asistencia escolar más alta o más baja? ¿Y esta asociación difiere según a qué escuela asisten los estudiantes? Averigüemos usando una gráfica de puntos.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()

'''
NOTA DE PLOT: Parece que los estudiantes en relaciones románticas tienen un promedio mayor y una mediana de ausencias en la escuela de medicina general, pero esta asociación no es válida para la escuela de EM

'''
