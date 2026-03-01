# Last updated: 3/1/2026, 10:35:07 AM
1import pandas as pd
2
3def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
4    products['quantity'] = products['quantity'].fillna(0)
5    return products