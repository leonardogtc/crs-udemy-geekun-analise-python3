import plotly.express as px
import pandas as pd
import plotly.io as pio


dados = {
    "fruta": ["Laranja", "Melancia", "Manga", "Jaca"],
    "porcentagem": [15, 30, 45, 10]
}

df = pd.DataFrame(data=dados)

fig = px.pie(
    df,
    values='porcentagem',
    names='fruta'
)

fig.update_layout(showlegend=False)

fig.update_traces(textinfo='percent+label')

fig.update_layout(hovermode=False)

# fig.show()

pio.write_image(fig, 'dataviz/s07-plotly/grafico1.png')
