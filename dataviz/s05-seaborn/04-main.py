import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

dados = {
    'Amostra_A': [1, 2, 4, 6],
    'Amostra_B': [2, 4, 8, 12],
    'Amostra_C': [4, 8, 16, 24],
}

""" Os indices são definidos porque o pandas inicia
    seus índices por zero (0) e o ponto seria marcado
    no eixo Y.
"""
indices = [1, 2, 3, 4]

# Criar um DATAFRAME para gerenciar os dados
df = pd.DataFrame(data=dados, index=indices)

# Desenhar o gráfico dos dados no DATAFRAME
plot = sns.lineplot(df)

plot.set_title('Dados das Amostras')
plot.set_xlabel('Tempo')
plot.set_ylabel('Concentração')

# Mostra o gráfico
plt.show()