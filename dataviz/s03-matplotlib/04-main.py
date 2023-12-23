# Import Library
import matplotlib.pyplot as plt

# Instance object figure
fig, ax = plt.subplots()

# define data
# axe x
indices = [1, 2, 3, 4]

# axe y
amostra_a = [1, 4, 2, 3]

# plot data on axes
ax.plot(indices, amostra_a)

# show figure
plt.show()
