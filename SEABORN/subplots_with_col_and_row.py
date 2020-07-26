'''
Crear subtramas con col y row
Hemos visto en ejercicios anteriores que los estudiantes con más ausencias ( "absences") tienden a tener calificaciones finales más bajas ( "G3"). ¿Esta relación se mantiene independientemente de cuánto tiempo estudien los estudiantes cada semana?

Para responder a esto, veremos la relación entre el número de ausencias que tiene un estudiante en la escuela y su calificación final en el curso, creando subtramas separadas basadas en el tiempo de estudio semanal de cada estudiante ( "study_time").

Seaborn ha sido importado como snsy matplotlib.pyplotha sido importado como plt.

'''
import seaborn as sns
import matplotlib.pyplot as plt

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            col="study_time",
            row="study_time")

# Show plot
plt.show()
