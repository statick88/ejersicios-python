
import datetime as dt
import matplotlib.pyplot as plt

hoy = dt.date.today()
print(f"Fecha de hoy: {hoy}")
fechas = [dt.date(2024, 1, 1), dt.date(2024, 2, 1), dt.date(2024, 3, 1)]
valores = [10, 20, 15]
plt.plot(fechas, valores)
plt.title("Valores a lo largo del tiempo")
plt.xlabel("Fecha")
plt.ylabel("Valor")
plt.show()
