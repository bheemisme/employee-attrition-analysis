from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_age_total_work_years
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_age_total_work_years(source)),
        id=ids.AGE_TOTAL_YEARS,
        className='w-50'
    )

