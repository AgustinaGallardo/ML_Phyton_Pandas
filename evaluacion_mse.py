import numpy as np

def mean_squared_error(y_true, y_pred):
    n = len(y_true)
    mse = np.sum((y_true - y_pred) ** 2) / n
    return mse

# Datos de ejemplo
y_true = np.array([2, 4, 6, 8, 10])
y_pred = np.array([2.1, 4.0, 5.9, 8.2, 9.8])

mse = mean_squared_error(y_true, y_pred)

print("Evaluación MSE")
print("Error Cuadrático Medio (MSE):", mse)