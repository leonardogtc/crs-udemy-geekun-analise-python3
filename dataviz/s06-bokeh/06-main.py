import bokeh.plotting as bkh
import numpy as np

pesquisa = np.random.normal(170, 10, 250)

hist, edges = np.histogram(pesquisa, density=True, bins=8)

fig = bkh.figure()

fig.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    line_color='#ffffff'
)

bkh.output_file('dataviz/s06-bokeh/index.html')

bkh.show(fig)
