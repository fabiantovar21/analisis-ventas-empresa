import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas = df.groupby("fecha")["total"].sum()

ventas.plot()

plt.title("Ventas por fecha")

plt.savefig("resultados/grafico_ventas.png")
