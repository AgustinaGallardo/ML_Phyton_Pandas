import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Leer datos del CSV
df = pd.read_csv('clientes.csv')

# Suponiendo que la columna 'responde_oferta' es la variable objetivo (0 o 1)
X = df[['edad', 'ingresos', 'historial_compras', 'frecuencia_compras']]
y = df['responde_oferta']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
print("Informe de Clasificación:")
print(classification_report(y_test, y_pred))