from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_working_groups
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_working_groups(source)),
        id=ids.WORKING_YEARS_MONTHLY_INCOME
    )

