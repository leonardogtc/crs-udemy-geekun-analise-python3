import pandas as pd
import matplotlib.pyplot as plt

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
df.plot.pie(y='Percentual', legend=False, autopct='%1.2f%%').set_ylabel('')

# mostra o gráfico
plt.show()
