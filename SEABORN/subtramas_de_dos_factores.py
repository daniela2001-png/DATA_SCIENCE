'''
Crear subtramas de dos factores
Continuemos mirando el student_dataconjunto de datos de estudiantes en la escuela secundaria. Aquí, queremos responder la siguiente pregunta: ¿la calificación del primer semestre de un estudiante ( "G1") tiende a correlacionarse con su calificación final ( "G3")?

Hay muchos aspectos de la vida de un estudiante que podrían resultar en una calificación final más alta o más baja en la clase. Por ejemplo, algunos estudiantes reciben apoyo educativo adicional de su escuela ( "schoolsup") o de su familia ( "famsup"), lo que podría resultar en calificaciones más altas. Intentemos controlar estos dos factores creando subtramas en función de si el estudiante recibió apoyo educativo adicional de su escuela o familia.

Seaborn ha sido importado como snsy matplotlib.pyplotha sido importado como plt.

'''
import seaborn as sns
import matplotlib as plt

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"], row='famsup', row_order=['yes', 'no'])

# Show plot
plt.show()

'''
OBERVACIONES DE LA TRAMA: Parece que la calificación del primer semestre se correlaciona con la calificación final, independientemente del tipo de apoyo que recibió el estudiante.

'''
