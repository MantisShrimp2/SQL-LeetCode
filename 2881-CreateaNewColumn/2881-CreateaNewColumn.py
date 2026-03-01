# Last updated: 3/1/2026, 10:12:04 AM
1import pandas as pd
2
3def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
4    return customers.drop_duplicates(subset='email',keep='first')
5    