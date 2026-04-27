# src/main.py

from extract.extract_csv import extract
from transform.transform_data import transform
from load.load_db import load

def run():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run()