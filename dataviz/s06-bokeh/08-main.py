import pandas as pd
import bokeh.plotting as bkh
from math import pi
from bokeh.transform import cumsum
from bokeh.io import export_png

x = {
    "Uva": 15,
    "Morango": 30,
    "Abacaxi": 45,
    "Mamão": 10
}

dados = pd.Series(x).reset_index(
    name='valor').rename(columns={'index': 'fruta'})
dados['angulo'] = dados['valor'] / dados['valor'].sum() * 2 * pi
dados['cor'] = ['#fa8d22', '#fd5532', '#069869', '#b9817b']

fig = bkh.figure(
    height=350,
    title='Título do Gráfico',
    toolbar_location=None,
    tools='hover',
    tooltips='@fruta: @valor%',
    x_range=(-0.5, 1.0)
)

fig.wedge(
    x=0,
    y=1,
    radius=0.4,
    start_angle=cumsum('angulo', include_zero=True),
    end_angle=cumsum('angulo'),
    line_color='#ffffff',
    fill_color='cor',
    legend_field='fruta',
    source=dados
)

fig.axis.axis_label = None
fig.axis.visible = False
fig.grid.grid_line_color = None

export_png(fig, filename='grafico1.png')
bkh.output_file('dataviz/s06-bokeh/index.html')
bkh.show(fig)
