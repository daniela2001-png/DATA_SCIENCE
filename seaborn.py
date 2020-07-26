'''
Hue y contar parcelas
Continuemos explorando nuestro conjunto de datos de los estudiantes de secundaria mirando una nueva variable.
La "school"columna indica las iniciales de la escuela a la que asistió el estudiante, ya sea "GP" o "MS".

En el último ejercicio, creamos un diagrama de dispersión donde los puntos del diagrama se colorearon en función de si el estudiante vivía en un área urbana o rural.
¿Cuántos estudiantes viven en áreas urbanas versus rurales,
y esto varía según la escuela a la que asiste el estudiante? Hagamos un diagrama de conteo con subgrupos para descubrirlo.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups

sns.countplot(x='school', hue='location', data=student_data, palette=palette_colors)


# Display plot
plt.show()



















