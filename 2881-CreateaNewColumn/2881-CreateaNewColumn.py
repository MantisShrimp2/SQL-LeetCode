# Last updated: 3/1/2026, 10:12:33 AM
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"], keep="first")