from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app



list_of_locations = {
    "All": 0,
    "Manhattan": 1,
    "Brooklyn": 2,
    "Bronx": 3,
    "Queens": 4,
    "Staten Island": 5
}

slider_size = [100, 500, 1000, 10000, 10000000]

controllers = dbc.Row([
    html.Img(id="logo", src=app.get_asset_url("logo_dark.png"),style={"width": "50%"}),
    html.H1("Venda de Imóveis - NYC", style={"margin-top": "20px"}),
    html.P(""" Utilize este dash para encontrar imóveis de alta qualidade no periodo de 1 ano."""),

    html.H1("""Distrito """, style={"margin-top": "50px", "margin-bottom": "25px"}),
    dcc.Dropdown(
        id="location-dropdown",
        options=[{"label":i, "value": j} for i, j in list_of_locations.items()],
        value=0,
        placeholder="Selecione um distrito"
    ),
    html.H4("""Metragem (m2)""", style={"margin-top": "20px", "margin-bottom": "25px"}),

    dcc.Slider(
        id="slider-square-size", min=0, max=4, step=1,
        marks={i: str(j) for i,j in enumerate(slider_size)},
        value=0,      
    ),
    html.H4("""Variável de Controle""", style={"margin-top": "20px", "margin-bottom": "25px"}),

    dcc.Dropdown(
        options=[
            {'label': 'YEAR BUILT', 'value': 'YEAR BUILT'},
            {'label': 'SALE PRICE', 'value': 'SALE PRICE'},
            {'label': 'TOTAL UNITS', 'value': 'TOTAL UNITS'},                 
        ],
        value='SALE PRICE',
        id='dropdown-color',
    ),

])