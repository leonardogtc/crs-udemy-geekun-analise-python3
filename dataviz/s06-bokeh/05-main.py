import bokeh.plotting as bkh

frutas = ["Laranja", "Melancia", "Manga", "Jaca"]
quantidades = [60, 100, 85, 30]
cores = ["#fa8d22", "#fd5532", "#069869", "#b9817b"]

fig = bkh.figure(
    title='Título do Gráfico',
    x_axis_label='Label X',
    y_axis_label='Label Y',
    x_range=frutas,
    width=1024,
    height=768
)

fig.vbar(
    x=frutas,
    top=quantidades,
    legend_label='Quantidades',
    width=0.5,
    bottom=0,
    color=cores
)

fig.legend.visible = False
fig.toolbar.logo = None
fig.toolbar_location = None


# bkh.output_file('dataviz/s06-bokeh/index.html')
bkh.show(fig)
