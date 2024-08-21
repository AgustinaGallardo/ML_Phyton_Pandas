from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Variables independientes
y = np.array([0, 0, 1, 1, 1])  # Variable dependiente (0 o 1)

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Ajustar el modelo a los datos
model.fit(X, y)

# Realizar predicciones
X_new = np.array([[6], [7]])  # Nuevos datos para predecir
predictions = model.predict(X_new)

print("Árboles de Decisión")
print("Predicciones:", predictions)  # Predicciones para los nuevos datos