from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_years_at_company_groups
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_years_at_company_groups(source)),
        id=ids.YEARS_AT_COMPANY_GROUPS,
        className='w-50'
    )

