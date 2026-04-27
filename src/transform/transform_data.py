def transform(df):
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Debug check
    print("Columns:", df.columns)

    df = df.dropna()

    if "name" not in df.columns:
        raise Exception("Column 'name' not found in data")

    df["name"] = df["name"].str.upper()

    return df