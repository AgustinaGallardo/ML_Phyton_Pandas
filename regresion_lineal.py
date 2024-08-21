from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])  # Variables independientes
y = np.array([2, 4, 6, 8, 10])  # Variable dependiente

# Crear el modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo a los datos
model.fit(X, y)

# Realizar predicciones
X_new = np.array([[6], [7]])  # Nuevos datos para predecir
predictions = model.predict(X_new)

print("Regresión Lineal")
print("Coeficientes:", model.coef_)  # Coeficientes de las variables independientes
print("Intercepto:", model.intercept_)  # Término de intercepción
print("Predicciones:", predictions)  # Predicciones para los nuevos datos