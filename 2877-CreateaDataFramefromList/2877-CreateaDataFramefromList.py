# Last updated: 3/1/2026, 9:55:30 AM
1import pandas as pd
2
3def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
4    rows = 3
5    return employees[0:rows]
6    