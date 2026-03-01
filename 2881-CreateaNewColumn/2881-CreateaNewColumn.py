# Last updated: 3/1/2026, 10:15:41 AM
1import pandas as pd
2
3def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
4    employees['salary'] = employees['salary']*2
5    return employees
6    