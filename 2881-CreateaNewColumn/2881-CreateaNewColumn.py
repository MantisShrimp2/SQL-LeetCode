# Last updated: 3/1/2026, 10:33:03 AM
1import pandas as pd
2
3def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
4    students = students.astype({'grade':'int'})
5    return students