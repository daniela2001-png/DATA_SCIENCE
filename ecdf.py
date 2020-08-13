# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor, label='CDF TEÓRICO')
plt.plot(x, y, marker='.', linestyle='none', label='CDF REAL')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')
plt.legend()
# Show the plot
plt.show()

'''
NOTA RESULTADO DE LA ECDF NORMAL Y TEORICA
Parece que los juegos sin hits en la era moderna de las Grandes Ligas se distribuyen exponencialmente.
Basado en la historia de la distribución exponencial, esto sugiere que son un proceso aleatorio;
cuándo ocurrirá un juego sin hits es independiente de cuándo fue el último juego sin hits.
'''
