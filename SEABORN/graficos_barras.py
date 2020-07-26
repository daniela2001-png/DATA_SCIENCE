'''
Gráficos de barras con porcentajes
Continuemos explorando las respuestas a una encuesta enviada a los jóvenes. La variable "Interested in Math"es Truesi la persona informó que estaba interesada o muy interesada en las matemáticas, y de lo Falsecontrario. ¿Qué porcentaje de jóvenes informan estar interesados ​​en las matemáticas, y esto varía según el género? Usemos un diagrama de barras para averiguarlo.

Como recordatorio, crearemos un diagrama de barras usando la catplot()función, proporcionando el nombre de la variable categórica para colocar en el eje x ( x=____), el nombre de la variable cuantitativa para resumir en el eje y ( y=____), el Marco de datos de Pandas utilizar ( data=____) y el tipo de trama categórica ( kind="bar").

Seaborn ha sido importado como snsy matplotlib.pyplotha sido importado como plt.

'''

# Create a bar plot of interest in math, separated by gender

sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')

# Show plot
plt.show()

'''
NOTA:  Cuando la variable y es Verdadero / Falso, los gráficos de barras mostrarán el porcentaje de respuestas que informan Verdadero. Este gráfico nos muestra que los hombres reportan un interés mucho mayor en las matemáticas en comparación con las mujeres.

'''
