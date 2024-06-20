from dash import Dash, html
from ..data.source import DataSource

# from src.components import ()


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, className="text-center text-primary"),
            html.Div(className="body-container", children=[

            ])
        ],
    )