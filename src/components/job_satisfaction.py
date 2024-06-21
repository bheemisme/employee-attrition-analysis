from dash import Dash, dcc, html
from ..data.source import DataSource
from ..data.charts import plot_employee_job_sat
from . import ids


def render(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        dcc.Graph(figure=plot_employee_job_sat(source)),
        id=ids.JOB_SATISFACTION
    )

