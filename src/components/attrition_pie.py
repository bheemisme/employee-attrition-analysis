from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_attrition_pie
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_attrition_pie(source)),
        id=ids.ATTRITION_PIECHART,
        className='w-50'
    )

