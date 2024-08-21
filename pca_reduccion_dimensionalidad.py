from sklearn.decomposition import PCA
import numpy as np

# Datos de ejemplo
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])  # Datos con 2 características

# Crear el modelo de PCA
pca = PCA(n_components=1)  # Reducir a 1 componente

# Ajustar el modelo a los datos
X_reduced = pca.fit_transform(X)

print("PCA - Reducción de Dimensionalidad")
print("Datos originales:\n", X)
print("Datos reducidos:\n", X_reduced)