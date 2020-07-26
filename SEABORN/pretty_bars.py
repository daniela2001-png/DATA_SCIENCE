'''
Personalizar diagramas de barras
En este ejercicio, exploraremos datos de estudiantes de secundaria. La "study_time"variable se guarda informado de tiempo de estudio semanal de cada estudiante como una de las siguientes categorías: "<2 hours", "2 to 5 hours", "5 to 10 hours", o ">10 hours". ¿Los estudiantes que reportan mayores cantidades de estudio tienden a obtener mejores calificaciones finales? Comparemos la calificación final promedio entre los estudiantes en cada categoría usando un diagrama de barras.

Seaborn ha sido importado como snsy matplotlib.pyplotha sido importado como plt.

'''

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"], ci=None)

# Show plot
plt.show()

'''
NOTA:  Los estudiantes de nuestra muestra que estudiaron más tienen una calificación promedio ligeramente más alta, pero no es una relación sólida.

'''
