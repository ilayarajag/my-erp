# src/extract/extract_csv.py

import pandas as pd

def extract():
    df = pd.read_csv("data/raw/users.csv")
    return df