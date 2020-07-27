'''
Ajustando los bigotes
En la lección vimos que hay múltiples formas de definir los bigotes en un diagrama de caja. En este conjunto de ejercicios, continuaremos usando el student_dataconjunto de datos para comparar la distribución de las calificaciones finales ( "G3") entre los estudiantes que tienen una relación romántica y los que no. Usaremos la "romantic"variable, que es un indicador de sí / no de si el estudiante está en una relación romántica.

Creemos un diagrama de caja para ver esta relación y probar diferentes formas de definir los bigotes.

Ya hemos importado Seaborn como snsy matplotlib.pyplotcomo plt.
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()

'''
OBSERVACION DE LA BOXPLOT: La calificación promedio es la misma entre estos dos grupos, pero la calificación máxima es más alta entre los estudiantes que no tienen una relación romántica.


'''
