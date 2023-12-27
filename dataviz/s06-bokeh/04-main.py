import bokeh.plotting as bkh

indices = [1, 2, 3, 4]
amostra_a = [1, 4, 2, 3]
amostra_b = [2, 8, 4, 6]
amostra_c = [4, 16, 8, 12]


fig = bkh.figure(
    title='Título do Gráfico',
    x_axis_label='Eixo X',
    y_axis_label='Eixo Y'
)

fig.line(
    x=indices,
    y=amostra_a,
    legend_label='Amostra A',
    color='blue',
    line_width=1
)

fig.line(
    x=indices,
    y=amostra_b,
    legend_label='Amostra B',
    color='red',
    line_width=2
)

fig.line(
    x=indices,
    y=amostra_c,
    legend_label='Amostra C',
    color='green',
    line_width=3
)

bkh.output_file('dataviz/s06-bokeh/index.html')

bkh.show(fig)
