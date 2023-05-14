# Obtener los datos del histograma
hist, bin_edges, _ = plt.hist(songs['danceability'], bins=20, density=True)
# Calcular la PDF y la CDF
pdf = hist / np.sum(hist)
cdf = np.cumsum(pdf)
# Definir el umbral de danzabilidad
umbral = 0.5
# Calcular la probabilidad de que una canción al azar sea bailable
probabilidad_bailable = 1 - cdf[np.searchsorted(bin_edges, umbral)]
print("La probabilidad solicitada: ", probabilidad_bailable)
porcentaje_bailable = probabilidad_bailable * 100
print("En porcentaje es :", porcentaje_bailable)