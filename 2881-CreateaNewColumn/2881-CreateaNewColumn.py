# Last updated: 3/1/2026, 10:24:51 AM
1import pandas as pd
2
3def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
4    col_dict= {'id':'student_id', 'first':'first_name','last':'last_name','age':'age_in_years'}
5    students = students.rename(columns=col_dict)
6    return students
7    