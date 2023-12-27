import seaborn as sns
import matplotlib.pyplot as plt

labels = ['laranja', 'melancia', 'manga', 'jaca']
percent = [15, 30, 45, 10]

cores = sns.color_palette('pastel')[0:5]

plt.pie(percent, colors=cores, labels=labels, autopct='%1.2f%%')

plt.show()
