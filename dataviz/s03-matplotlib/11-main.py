# Gráfico de Pizza (pie)
import matplotlib.pyplot as plt
from pathlib import Path

image_dir = Path.cwd() / 'dataviz/s03-matplotlib/images'
print(f"Image Dir: {image_dir}") 

fig, ax = plt.subplots()

labels = ['laranja', 'melancia', 'manga', 'jaca']
percent = [15, 30, 45, 10]

ax.pie(percent, labels=labels, autopct='%1.2f%%')

fig.savefig(
    image_dir/'meu_grafico_2.png',
    transparent=True,
    dpi=150,
    bbox_inches='tight'
    )

fig.savefig(
    image_dir/'meu_grafico_3.pdf',
    transparent=True,
    dpi=150,
    bbox_inches='tight'
    )

# Extra - Função para mostrar todos os formatos:
print(f"Formatos: {fig.canvas.get_supported_filetypes()}")

# plt.show()