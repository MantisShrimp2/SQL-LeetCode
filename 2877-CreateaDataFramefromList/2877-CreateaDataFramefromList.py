# Last updated: 3/1/2026, 9:43:57 AM
1import pandas as pd
2
3def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
4
5    df = pd.DataFrame(data=student_data, columns=['student_id','age'])
6    return df