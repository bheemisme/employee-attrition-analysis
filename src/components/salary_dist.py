from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_salary_distribution
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_salary_distribution(source)),
        id=ids.SALARY_DISTRIBUTION,
        className='w-50'
    )

