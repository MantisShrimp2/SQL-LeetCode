# Last updated: 3/1/2026, 10:37:16 AM
1import pandas as pd
2
3def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
4    conc = pd.concat([df1,df2])
5    return conc