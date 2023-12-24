
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Amostra A": [1, 4, 2, 3],
    "Amostra B": [2, 8, 4, 6],
    "Amostra C": [4, 16, 8, 12],
    }
indices = [1, 2, 3, 4]

df = pd.DataFrame(data=dados, index=indices)
# print(f"DataFrame: {df}")

df.plot.line(
    title="Título do Gráfico",
    ylabel='Eixo Y',
    xlabel='Eixo X'
)
plt.show()
