# histograma
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

pesquisa = np.random.normal(170, 10, 250)
# print(f"{pesquisa}")
ax.hist(pesquisa, bins=8, linewidth=0.5, edgecolor='#fff')

plt.show()
