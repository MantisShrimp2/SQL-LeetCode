# Last updated: 3/1/2026, 10:14:34 AM
1import pandas as pd
2
3def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
4    return students.dropna(subset='name')