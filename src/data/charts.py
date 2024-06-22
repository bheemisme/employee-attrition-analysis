import seaborn as sns
import matplotlib.pyplot as plt
from .source import DataSource
from .loader import DataSchema

import plotly.express as px
import plotly.graph_objects as go

import numpy as np


def plot_age_distribution(ds: DataSource) -> go.Figure:

    fig = px.histogram(
        data_frame=ds.df,
        x=DataSchema.age_groups,
        color_discrete_sequence=["#3cc389"],
        histfunc="count",
        title="Age Distribution",
        category_orders={
            DataSchema.age_groups: ds.sorted_age_groups()
        }
    )

    fig.update_layout(yaxis_title="No. of employees", xaxis_title="Age")
    return fig


def plot_salary_distribution(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        data_frame=ds.df,
        x=DataSchema.salary_groups,
        color=DataSchema.attrition,
        histfunc="count",
        category_orders={
            DataSchema.salary_groups: ds.sorted_salary_groups()
        },

        barmode="group",
        title="Salary Distribution"
    )

    fig.update_layout(yaxis_title="No. of employees",
                      xaxis_title="Monthly Income")
    return fig


def plot_working_years_distribution(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        data_frame=ds.df,
        x=DataSchema.working_year_groups,
        color=DataSchema.attrition,
        histfunc='count',
        category_orders={
            DataSchema.working_year_groups: ds.sorted_salary_groups()
        },
        barmode="overlay",
        title="Total Working Years"

    )
    fig.update_layout(yaxis_title="No. of employees",
                      xaxis_title="Total Working Years")
    return fig


def plot_years_at_company(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        data_frame=ds.df,
        x=DataSchema.years_at_company_groups,
        color=DataSchema.attrition,
        histfunc="count",
        category_orders={
            DataSchema.years_at_company: ds.sorted_years_at_company_groups(),
        },
        barmode="group",
        title="Years At Company"
    )

    fig.update_layout(yaxis_title="No. of employees",
                      xaxis_title="Years At Company")
    return fig


def plot_departments_table(ds: DataSource) -> go.Figure:

    depts = ds.df[DataSchema.department].unique()
    depts.sort()

    l_values = ds.get_attrition("Yes").groupby(by=[DataSchema.department]).count()[
        DataSchema.employee_id].to_numpy()
    s_values = ds.get_attrition("No").groupby(by=[DataSchema.department]).count()[
        DataSchema.employee_id].to_numpy()

    fig = go.Figure(data=[go.Table(
        header=dict(values=["Department", "Leaving", "Staying"]),
        cells=dict(values=[depts, l_values, s_values]),
    )])
    fig.update_layout(title_text="Departments")
    return fig


def plot_employee_env_sat(ds: DataSource) -> go.Figure:

    fig = px.parallel_categories(ds.df, dimensions=[DataSchema.department,
                                                    DataSchema.environment_satisfaction,
                                                    DataSchema.attrition
                                                    ])

    fig.update_layout(title_text="Environment Satisfaction")

    return fig


def plot_employee_job_sat(ds: DataSource) -> go.Figure:

    fig = px.parallel_categories(ds.df, dimensions=[
        DataSchema.department,
        DataSchema.job_satisfaction,
        DataSchema.attrition
    ])

    fig.update_layout(title_text="Job Satisfaction")

    return fig


def plot_working_groups(ds: DataSource) -> go.Figure:

    fig = px.box(ds.df,
                 x=DataSchema.working_year_groups,
                 y=DataSchema.monthly_income,
                 color=DataSchema.attrition
                )

    fig.update_layout(
        title_text='Working Groups - Monthly Income',
        xaxis_title_text="Working Years",
        yaxis_title_text="Monthly Income"
    )

    return fig


def plot_years_at_company_groups(ds: DataSource) -> go.Figure:
    fig = px.box(ds.df, x=DataSchema.years_at_company_groups,
                 y=DataSchema.monthly_income, color=DataSchema.attrition)

    fig.update_layout(
        title_text="Years At Company - Monthly Income",
        xaxis_title="Years At Company",
        yaxis_title="Monthly Income"
    )

    return fig


def plot_age_monthly_income(ds: DataSource) -> go.Figure:
    fig = px.histogram(ds.df,
                       x=DataSchema.age_groups,
                       y=DataSchema.monthly_income,
                       color=DataSchema.attrition,
                       histfunc="avg",
                       barmode="overlay"
                       )

    fig.update_layout(
        title_text="Age - Monthly Income",
        xaxis_title="Age",
        yaxis_title="Monthly Income"
    )

    return fig


def plot_age_total_work_years(ds: DataSource) -> go.Figure:
    fig = px.histogram(ds.df,
                       x=DataSchema.age_groups,
                       y=DataSchema.total_working_years,
                       color=DataSchema.attrition,
                       histfunc="avg",
                       barmode="overlay"
                       )

    fig.update_layout(
        title_text="Age - Total Working Years",
        xaxis_title="Age",
        yaxis_title="Total Working Years"
    )

    return fig


def plot_age_years_at_company(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        ds.df,
        x=DataSchema.age_groups,
        y=DataSchema.years_at_company,
        color=DataSchema.attrition,
        histfunc="avg",
        barmode="overlay"
    )

    fig.update_layout(
        title_text="Age - Years At Company",
        xaxis_title="Age",
        yaxis_title="Years At Company"
    )

    return fig


def plot_years_at_company_monthly_income(ds: DataSource) -> go.Figure:
    fig = px.histogram(
        ds.df,
        x=DataSchema.years_at_company_groups,
        y=DataSchema.monthly_income,
        color=DataSchema.attrition,
        histfunc="avg",
        barmode="overlay"
    )

    fig.update_layout(
        title_text="Years At Company - Monthly Income",
        xaxis_title="Years At Company",
        yaxis_title="Monthly Income"
    )

    return fig


def plot_education_attrition(ds: DataSource) -> go.Figure:
    fig = px.parallel_categories(
        ds.df,
        dimensions=[
            DataSchema.education_field,
            DataSchema.education,
            DataSchema.attrition
        ]
    )
    fig.update_layout(
        title_text="Education - Attrition"
    )
    return fig
