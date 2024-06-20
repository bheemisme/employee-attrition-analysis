from functools import reduce
from typing import Callable

import numpy as np
import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


class DataSchema:
    employee_id = "EmployeeID"
    age = "Age"
    attrition = "Attrition"
    business_travel = "BusinessTravel"
    department = "Department"
    distance_from_home = "DistanceFromHome"
    education = "Education"
    education_field = "EducationField"
    employee_count = "EmployeeCount"
    gender = "Gender"
    job_level = "JobLevel"
    job_role = "JobRole"
    marital_status = "MaritalStatus"
    monthly_income = "MonthlyIncome"
    num_companies_worked = "NumCompaniesWorked"
    over_18 = "Over18"
    percent_salary_hike = "PercentSalaryHike"
    standard_hours = "StandardHours"
    stock_option_level = "StockOptionLevel"
    total_working_years = "TotalWorkingYears"
    training_times_last_year = "TrainingTimesLastYear"
    years_at_company = "YearsAtCompany"
    years_since_last_promotion = "YearsSinceLastPromotion"
    years_with_curr_manager = "YearsWithCurrManager"
    environment_satisfaction = "EnvironmentSatisfaction"
    job_satisfaction = "JobSatisfaction"
    work_life_balance = "WorkLieBalance"
    job_involvement = "JobInvolvemnet"
    performance_rating = "PerformanceRating"
    age_group = "age_group"



def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=False)

def iqr_cleaning(df: pd.DataFrame, attr: str, thresh = 0) -> pd.DataFrame:
    if df[attr].dtype == np.float64 or df[attr].dtype == np.float32 or df[attr].dtype == np.int64 or df[attr].dtype == np.int32:
        q1, q2, q3 = df[attr].quantile([.25,.5,.75])
        iqr = q3 - q1
        return df[(df[attr] >= q1 - thresh * iqr) & (df[attr] <= q3 + thresh * iqr)]
    raise ValueError("attr should be of float or int dtype")

def drop_attributes(df: pd.DataFrame) -> pd.DataFrame:
    
    global dropped_attributes
    dropped_attributes = [
        DataSchema.over_18,
        DataSchema.standard_hours,
        DataSchema.employee_count,
        DataSchema.gender,
        DataSchema.distance_from_home,
        DataSchema.business_travel,
        DataSchema.stock_option_level,
        DataSchema.years_with_curr_manager,
        DataSchema.marital_status,
    ]
    
    df = df.drop(labels=dropped_attributes, axis=1, errors="ignore")
    return df


def relabel_gender(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.gender] = df[DataSchema.gender].map({0: 'Female', 1: "Male"})
    return df


def relabel_attrition(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.attrition] = df[DataSchema.attrition].map(
        {
            1: 'Positive',
            0: "Negative"
         })
    return df


def add_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.age_group] = pd.cut(df[DataSchema.age], bins=[20, 30, 40, 50, 60, 70, 80])
    df[DataSchema.age_group] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.age_group])))
    return df


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def load_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path
    )
    preprocessor = compose(
        remove_duplicates,
        relabel_gender,
        relabel_attrition,
        add_age_groups,
        drop_attributes
    )
    return preprocessor(data)
