from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_education_attrition
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_education_attrition(source)),
        id=ids.YEARS_AT_COMPANY_MONTHLY_INCOME
    )

