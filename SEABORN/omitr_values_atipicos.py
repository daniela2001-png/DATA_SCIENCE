'''
Omitir valores atípicos
Ahora usemos el student_dataconjunto de datos para comparar la distribución de las calificaciones finales ( "G3") entre los estudiantes que tienen acceso a Internet en casa y los que no. Para hacer esto, usaremos la "internet"variable, que es un indicador binario (sí / no) de si el estudiante tiene acceso a Internet en casa.

Dado que Internet puede ser menos accesible en las zonas rurales, agregaremos subgrupos según el lugar donde viva el estudiante. Para esto, podemos usar la "location"variable, que es un indicador de si un estudiante vive en una ubicación urbana ("Urbana") o rural ("Rural").

Seaborn ya se ha importado como snsy matplotlib.pyplotse ha importado como plt. Como recordatorio, puede omitir valores atípicos en diagramas de caja configurando el symparámetro igual a una cadena vacía ( "").
'''
# Create a box plot with subgroups and omit the outliers

sns.catplot(x='internet', y='G3', kind='box', hue='location', data=student_data, sym='')




# Show plot
plt.show()
