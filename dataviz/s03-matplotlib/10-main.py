# Gráfico de Pizza (pie)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

labels = ['laranja', 'melancia', 'manga', 'jaca']
percent = [15, 30, 45, 10]

ax.pie(percent, labels=labels, autopct='%1.2f%%')

plt.show()
