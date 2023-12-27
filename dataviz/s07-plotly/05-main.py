import plotly.express as px

frutas = ['Laranja', 'Melancia', 'Manga', 'Jaca']
quantidades = [60, 100, 85, 30]

fig = px.bar(
    x=frutas,
    y=quantidades,
    title='Título do Gráfico',
    color=frutas,
    labels=dict(y='Label Y', x='Label X', color='Frutas')
)

fig.show()
