from sklearn.cluster import KMeans
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Datos para agrupar

# Crear el modelo de K-Means
model = KMeans(n_clusters=2)  # Número de clusters

# Ajustar el modelo a los datos
model.fit(X)

# Obtener las etiquetas de los clusters
labels = model.labels_

print("K-Means Clustering")
print("Etiquetas de los clusters:", labels)  # Etiquetas para cada punto de datos