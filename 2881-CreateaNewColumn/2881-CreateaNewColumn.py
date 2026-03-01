# Last updated: 3/1/2026, 10:53:13 AM
1import pandas as pd
2
3def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
4    heavy = animals[animals['weight'] >= 100].sort_values('weight',ascending=False)[['name']]
5    return heavy