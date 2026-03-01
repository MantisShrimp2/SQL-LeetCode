# Last updated: 3/1/2026, 10:05:36 AM
1import pandas as pd
2
3def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
4    bon_val = 2*employees['salary']
5
6    employees.insert(loc=2, column='bonus',value =bon_val)
7    return employees