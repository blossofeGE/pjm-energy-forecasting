import pandas as pd

def load_pjm_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)  
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame()

    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime")
    df = df.sort_index()

    df = df.groupby(level="Datetime").mean()
    df = df.asfreq('h')
    df = df.interpolate(method="linear")

    return df

if __name__ == "__main__":
    path = ("data/AEP_hourly.csv")
    data = load_pjm_data(path)

    if not data.empty:
        print(f"{data.index[0]},\n{data.index[-1]},\n{data.head()}")
    