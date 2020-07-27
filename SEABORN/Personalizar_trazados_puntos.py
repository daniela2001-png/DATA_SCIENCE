'''
Personalizar trazados de puntos
Continuemos mirando los datos de los estudiantes en la escuela secundaria, esta vez usando un diagrama de puntos para responder la pregunta: ¿la calidad de la relación familiar del estudiante influye en el número de ausencias que tiene el estudiante en la escuela? Aquí, usaremos la "famrel"variable, que describe la calidad de la relación familiar de un estudiante de 1 (muy malo) a 5 (muy bueno).

Como recordatorio, para crear un gráfico de puntos, use la catplot()función y especifique el nombre de la variable categórica para colocar en el eje x ( x=____), el nombre de la variable cuantitativa para resumir en el eje y ( y=____), el Marco de datos de Pandas utilizar ( data=____) y el tipo de trama categórica ( kind="point").

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.

'''

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join=False)
            
# Show plot
plt.show()

'''

Si bien el número promedio de ausencias es ligeramente menor entre los estudiantes con relaciones familiares de mayor calidad, los grandes intervalos de confianza nos dicen que no podemos estar seguros de que haya una asociación real aquí.

'''
