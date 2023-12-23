# Import Library
import matplotlib.pyplot as plt

# Instance object figure
fig, ax = plt.subplots()

# define data

# Dados
indices = [1, 2, 3, 4]
amostra_a = [1, 4, 2, 3]
amostra_b = [2, 8, 4, 6]
amostra_c = [4, 16, 8, 12]

# plot data on axes
ax.plot(indices, amostra_a, label="Amostra A", marker='.')
ax.plot(indices, amostra_b, label="Amostra B", marker='.')
ax.plot(indices, amostra_c, label="Amostra C", marker='.')

ax.legend()

# show figure
plt.show()
