'''

Crear e interpretar un diagrama de caja
Continuemos usando el student_dataconjunto de datos. En un ejercicio anterior, exploramos la relación entre el estudio y la calificación final mediante el uso de un gráfico de barras para comparar la calificación final promedio ( "G3") entre los estudiantes en diferentes categorías de "study_time".

En este ejercicio, intentaremos usar un diagrama de caja para ver esta relación. Como recordatorio, para crear un diagrama de caja necesitará usar la catplot()función y especificar el nombre de la variable categórica para colocar en el eje x ( x=____), el nombre de la variable cuantitativa para resumir en el eje y ( y=____) , el Pandas DataFrame para usar ( data=____) y el tipo de diagrama ( kind="box").

Ya hemos importado matplotlib.pyplotcomo plty seaborncomo sns.

'''

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories

sns.catplot(x='study_time', y='G3', data=student_data, kind='box', order=study_time_order)



# Show plot
plt.show()

