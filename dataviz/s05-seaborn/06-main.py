import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pesquisa = np.random.normal(170, 10, 250)

df = pd.DataFrame(data=pesquisa)

sns.histplot(
    df,
    bins=8,
    linewidth=0.5,
    edgecolor='#fff',
    legend=False 
)

plt.show()