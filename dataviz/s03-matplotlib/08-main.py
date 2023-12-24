# Gráfico de Barras
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

frutas = ['laranja', 'melancia', 'manga', 'jaca']
quantidades = [60, 100, 85, 30]

ax.bar(frutas, quantidades, label='Quantidade')
ax.set_xlabel('Frutas')
ax.set_ylabel('Quantidade')
ax.legend()

plt.show()
