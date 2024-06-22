from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_age_years_at_company
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_age_years_at_company(source)),
        id=ids.AGE_YEARS_AT_COMPANY
    )

