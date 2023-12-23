# Import Library
import matplotlib.pyplot as plt

# Instance object figure
fig, ax = plt.subplots()

'''
1. Define os valores das amostras, que tem que ser obrigatóriamente
um ArrayLike... isso corresponde a uma lista, uma tupla, qualquer
coisa que tenha o formato de conjuntos.
2. Esses conjuntos são de uma relação 1 para 1 e tem que ter 
obrigatoriamente o mesmo número de elementos.
'''
indices = [1, 2, 3, 4]
amostra_a = [1, 4, 2, 3]

'''
3. Plotando os dados na figura: A posição indices e amostra_a
correspondem a X e Y no eixo cartesiano! O Label definido aqui
tem que ser habilitado pela função legend() em algum lugar 
abaixo.
'''
ax.plot(indices, amostra_a, label="Amostra A", color='#0B8215', marker='.')
ax.set_title("Título do Gráfico")
ax.set_xlabel("Label X")
ax.set_ylabel('Label Y')

# Habilita a exibição da legenda na chamada.
ax.legend()

# show figure
plt.show()
