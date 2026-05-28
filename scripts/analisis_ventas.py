import pandas as pd

df = pd.read_csv("datos/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

print("Ventas totales:", ventas_totales)
print("Producto mas vendido:", producto_mas_vendido)
