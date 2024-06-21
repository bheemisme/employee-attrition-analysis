from functools import reduce
from typing import Callable

import numpy as np
import pandas as pd
import math
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
    age_groups = "ageGroups"
    salary_groups = "salaryGroups"
    working_year_groups = "workingYearGroups"
    years_at_company_groups = "YearsAtCompanyGroups"

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
    


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=False)

def iqr_cleaning(df: pd.DataFrame, attr: str, thresh = 0) -> pd.DataFrame:
    if df[attr].dtype == np.float64 or df[attr].dtype == np.float32 or df[attr].dtype == np.int64 or df[attr].dtype == np.int32:
        q1, q2, q3 = df[attr].quantile([.25,.5,.75])
        iqr = q3 - q1
        return df[(df[attr] >= q1 - thresh * iqr) & (df[attr] <= q3 + thresh * iqr)]
    raise ValueError("attr should be of float or int dtype")

def drop_attributes(df: pd.DataFrame) -> pd.DataFrame:    
    df = df.drop(labels=dropped_attributes, axis=1, errors="ignore")
    return df




def add_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    min_age, max_age = df[DataSchema.age].min(), df[DataSchema.age].max()
    
    age_groups_list = list(range(math.floor(min_age/5)*5, math.floor(max_age/5)*5+5,5))
    df[DataSchema.age_groups] = pd.cut(
                                        df[DataSchema.age],
                                       age_groups_list,
                                       )
    df[DataSchema.age_groups] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.age_groups])))
    return df

def add_salary_groups(df: pd.DataFrame) -> pd.DataFrame:
    min_salary, max_salary = df[DataSchema.monthly_income].min(), df[DataSchema.monthly_income].max()
    salary_groups_list = list(range(min_salary, max_salary+10000,10000))
    df[DataSchema.salary_groups] = pd.cut(df[DataSchema.monthly_income],salary_groups_list,include_lowest=True)
    df[DataSchema.salary_groups] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.salary_groups])))

    return df

def add_working_year_groups(df: pd.DataFrame) -> pd.DataFrame:

    min_work_years , max_work_years = int(df[DataSchema.total_working_years].min()), int(df[DataSchema.total_working_years].max())
    df[DataSchema.working_year_groups] = pd.cut(df[DataSchema.total_working_years], range(min_work_years,max_work_years+5,5), include_lowest=True)
    df[DataSchema.working_year_groups] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.working_year_groups])))
    
    return df

def add_years_at_company_groups(df: pd.DataFrame) -> pd.DataFrame:
    min_cmp_years , max_cmp_years = int(df[DataSchema.years_at_company].min()), int(df[DataSchema.years_at_company].max())
    df[DataSchema.years_at_company_groups] = pd.cut(df[DataSchema.years_at_company],range(min_cmp_years,max_cmp_years+5,5),include_lowest=True)
    df[DataSchema.years_at_company_groups] = pd.Series(list(map(lambda x: f'{x.left}-{x.right}', df[DataSchema.years_at_company_groups])))
    
    return df

def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

def drop_na(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def load_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path
    )
    preprocessor = compose(
        drop_na,
        remove_duplicates,
        drop_attributes,
        add_age_groups,
        add_salary_groups,
        add_working_year_groups,
        add_years_at_company_groups
    )
    return preprocessor(data)
