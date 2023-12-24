import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

image_dir = Path.cwd() / 'images'

dados = {
    "Percentual": [60, 100, 85, 30]
}

indices = ["Laranja", "Malancia", "Manga", "Jaca"]

df = pd.DataFrame(data=dados, index=indices)

print(f"DataFrame: {df}")

# Gera um erro sem as configurações
# df.plot.pie()

# Solução 1
# df.plot.pie(subplots=True)

# Solução 2 - Retira a legenda e configura Y como vazio
plot = df.plot.pie(y='Percentual', legend=False, autopct='%1.2f%%')
plot.set_ylabel('')

# Salva a figura
plot.get_figure().savefig(
    image_dir/'meu_grafico_1.png',
    # transparent=True,
    dpi=150,
    bbox_inches='tight'
)

# mostra o gráfico
# plt.show()
