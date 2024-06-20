from __future__ import annotations

from dataclasses import dataclass
from typing import List

import pandas as pd

from .loader import DataSchema, dropped_attributes


@dataclass
class DataSource:
    _data: pd.DataFrame

    @property
    def df(self) -> pd.DataFrame:
        return self._data

    def get_continous_attributes(self) -> List[str]:

        continous = [
            DataSchema.percent_salary_hike,
            DataSchema.num_companies_worked,
            DataSchema.total_working_years,
            DataSchema.years_at_company,
            DataSchema.training_times_last_year,
            DataSchema.monthly_income
        ]

        return continous

    def get_discrete_attributes(self) -> List[str]:

        discrete = [
            DataSchema.performance_rating,
            DataSchema.job_satisfaction,
            DataSchema.job_involvement,
            DataSchema.environment_satisfaction,
            DataSchema.work_life_balance,
            DataSchema.age_group
        ]

        return discrete

    def get_dropped_attributes(self) -> List[str]:
        return dropped_attributes


def sorted_age_groups(self):
    groups = self._data[DataSchema.age_group].unique()
    groups.sort()
    return groups
