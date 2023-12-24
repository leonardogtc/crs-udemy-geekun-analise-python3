import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Frutas": ["Laranja", "Malancia", "Manga", "Jaca"],
    'Quantidades': [60, 100, 85, 30]
}

df = pd.DataFrame(data=dados)
df.plot.bar(x='Frutas', y='Quantidades', rot=0)
plt.show()
