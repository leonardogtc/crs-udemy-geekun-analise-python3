# Import Library
import matplotlib.pyplot as plt

# Instance object figure
# fig, ax = plt.subplots()
fig, ax = plt.subplots(1, 2)

# define data

# Dados
indices = [1, 2, 3, 4]
amostra_a = [1, 4, 2, 3]
amostra_b = [2, 8, 4, 6]

ax[0].set_title('Pessoas')
ax[1].set_title('Cachorros')

# plot data on axes
ax[0].plot(indices, amostra_a, label="Amostra A", marker='.')
ax[1].plot(indices, amostra_b, label="Amostra B", color='green', marker='.')

ax[0].legend()
ax[1].legend()

# show figure
plt.show()
