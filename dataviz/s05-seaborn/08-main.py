import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

image_dir = Path.cwd() / 'dataviz/s05-seaborn/images'

labels = ['laranja', 'melancia', 'manga', 'jaca']
percent = [15, 30, 45, 10]

cores = sns.color_palette('pastel')[0:5]

plt.pie(percent, colors=cores, labels=labels, autopct='%1.2f%%')

plt.savefig(
    image_dir/'meu_grafico_1.png',
    transparent=True,
    dpi=150,
    bbox_inches='tight'
    )

# plt.show()