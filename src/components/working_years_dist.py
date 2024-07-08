from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_working_years_distribution
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        html.Div(
            children=[
                dcc.Graph(figure=plot_working_years_distribution(source)),
            ]
        ),
        id=ids.WORKING_YEARS,
        className='w-50'
    )

