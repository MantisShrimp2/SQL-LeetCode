# Last updated: 3/1/2026, 9:56:19 AM
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[0:3,:]