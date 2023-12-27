import plotly.express as px
import numpy as np

pesquisa = np.random.normal(170, 10, 250)

fig = px.histogram(
    pesquisa,
    nbins=8,
    title='Título do Gráfico'
)

fig.update_layout(showlegend=False)

fig.update_xaxes(title_text='Label X')
fig.update_yaxes(title_text='Label Y')

fig.update_traces(marker_line_width=0.5, marker_line_color='#ffffff')

fig.show()
