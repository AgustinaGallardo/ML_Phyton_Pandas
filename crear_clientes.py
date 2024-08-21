import pandas as pd

# Crear un DataFrame con los datos ficticios
data = {
    'edad': [25, 34, 45, 23, 50, 29, 31, 40, 36, 28],
    'ingresos': [50000, 60000, 80000, 40000, 70000, 55000, 62000, 75000, 67000, 53000],
    'historial_compras': [3, 2, 5, 1, 4, 3, 2, 4, 3, 1],
    'frecuencia_compras': [5, 3, 6, 4, 5, 2, 6, 7, 4, 2],
    'responde_oferta': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('clientes.csv', index=False)