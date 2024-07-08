from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_years_at_company
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        html.Div(
            children=[
                dcc.Graph(figure=plot_years_at_company(source)),
            ]
        ),
        id=ids.YEARS_AT_COMPANY,
        className='w-50'
    )

