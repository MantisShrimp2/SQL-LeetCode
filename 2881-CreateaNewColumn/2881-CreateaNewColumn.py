# Last updated: 3/1/2026, 10:45:27 AM
1import pandas as pd
2
3def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
4    return weather.pivot(index='month', columns='city')['temperature']
5    