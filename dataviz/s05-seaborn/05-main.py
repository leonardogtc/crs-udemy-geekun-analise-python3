import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# sns.set_theme('notebook')
# sns.set_style('darkgrid')

dados = {
    "Frutas": ["Laranja", "Malancia", "Manga", "Jaca"],
    'Quantidades': [60, 100, 85, 30]
}

df = pd.DataFrame(data=dados)

sns.barplot(df, x='Frutas', y='Quantidades')

plt.show()
