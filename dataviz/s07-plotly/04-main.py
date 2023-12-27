import plotly.express as px

indices = [1, 2, 3, 4]
amostras = [
    [1, 4, 2, 3],
    [2, 8, 4, 6],
    [4, 16, 8, 12]
]

fig = px.line(
    x=indices,
    y=amostras,
    title='Título do Gráfico',
    labels=dict(
        value='Label Y',
        x='Label X',
        variable='Amostras'
    )
)

fig.data[0].name = 'Amostra A'
fig.data[1].name = 'Amostra B'
fig.data[2].name = 'Amostra C'

fig.show()
fig.update_layout(showlegend=False)
fig.show(
    config=dict(displayModeBar=False)
)

# fig.show(config={'displayModeBar': False})
