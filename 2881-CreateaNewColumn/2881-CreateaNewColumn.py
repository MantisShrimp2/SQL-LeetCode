# Last updated: 3/1/2026, 10:48:46 AM
1import pandas as pd
2
3def meltTable(report: pd.DataFrame) -> pd.DataFrame:
4   return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')