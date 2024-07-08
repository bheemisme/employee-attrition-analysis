from dash import Dash, html
from ..data.source import DataSource

from src.components import (
    age_dist,
    dept_tables,
    emp_env_sat,
    job_satisfaction,
    salary_dist,
    working_groups_monthly_income,
    working_years_dist,
    year_at_company_dist,
    years_at_company_groups,
    age_monthly_income,
    age_years_at_company,
    years_monthly_income,
    age_total_years,
    attrition_pie
)


def create_layout(app: Dash, source: DataSource) -> html.Div:

    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title, className="text-center text-primary"),
            html.Div(className="body-container px-sm py-md", children=[
                html.Nav(className="navbar d-flex flex-row justify-content-around align-items-center",
                         children=[
                         ]),
                html.Div(className="chart-container d-flex flex-row align-items-center flex-wrap",
                         children=[
                             age_dist.render(app, source),
                             attrition_pie.render(app, source),
                             dept_tables.render(app, source),
                             salary_dist.render(app, source),
                             working_groups_monthly_income.render(app, source),
                             working_years_dist.render(app, source),
                             year_at_company_dist.render(app, source),
                             years_at_company_groups.render(app, source),
                             age_monthly_income.render(app, source),
                             age_years_at_company.render(app, source),
                             years_monthly_income.render(app, source),
                             age_total_years.render(app, source),
                             emp_env_sat.render(app, source),
                             job_satisfaction.render(app, source),

                         ])
            ])
        ],
    )
