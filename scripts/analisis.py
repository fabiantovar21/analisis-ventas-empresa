
import pandas as pd

datos = {
    "producto": ["Mouse", "Teclado", "Monitor"],
    "ventas": [10, 5, 3]
}

df = pd.DataFrame(datos)

print(df)

print("Ventas totales:", df["ventas"].sum())
