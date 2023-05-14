# Se realiza el histograma del primer parámetro musical y se configuran
# Títulos,eje y y eje x.
plt.hist(songs['danceability'], bins=20, density=True)
plt.title('Densidad de probabilidad de danzabilidad')
plt.xlabel('Calificación de bailabilidad')
plt.ylabel('Frecuencia Relativa')
# Mostrar el histograma
plt.show()
# Se crea asigna la columna que se le aplicará el mejor ajuste y
# Se recorren todas las distribuciones para encontrar las mejores
# Curvas.
p1 = Fitter(songs['danceability'].dropna())
p1.fit()
p1.summary()
# La función get_best() permite encontrar el mejor ajuste e imprimir sus
# Parámetros.
p1.get_best()
plt.savefig('p1.svg', transparent=True)
figura(hacer, 'p1.tex')