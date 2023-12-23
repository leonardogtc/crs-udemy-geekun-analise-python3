# Import Library
import matplotlib.pyplot as plt

# Instance object figure
# fig, ax = plt.subplots()
fig, ax = plt.subplots(2, 2)

# define data

# Dados
indices = [1, 2, 3, 4]
sample_a = [1, 4, 2, 3]
sample_b = [2, 8, 4, 6]
sample_c = [5, 12, 7, 9]
sample_d = [12, 8, 4, 6]

ax[0][0].set_title('06:00 - 12:00')
ax[0][1].set_title('12:00 - 18:00')
ax[1][0].set_title('18:00 - 00:00')
ax[1][1].set_title('00:00 - 06:00')

# plot data on axes
ax[0][0].plot(indices, sample_a, label="sample A", marker='o')
ax[0][1].plot(indices, sample_b, label="sample B", color='green', marker='o')
ax[1][0].plot(indices, sample_c, label="sample C", color='red', marker='o')
ax[1][1].plot(indices, sample_d, label="sample D", color='yellow', marker='o')

ax[0][0].legend()
ax[0][1].legend()
ax[1][0].legend()
ax[1][1].legend()

# show figure
plt.show()
