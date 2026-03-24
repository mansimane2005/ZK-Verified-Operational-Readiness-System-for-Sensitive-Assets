import pandas as pd
import numpy as np


def load_data(path):
    df = pd.read_csv(path, sep=" ", header=None)
    df = df.dropna(axis=1)
    return df


def prepare_dataset(path):
    df = load_data(path)

    # Remaining Useful Life (RUL)
    max_cycle = df.groupby(0)[1].max()
    rul = []

    for i in range(len(df)):
        engine = df.iloc[i, 0]
        cycle = df.iloc[i, 1]
        rul.append(max_cycle[engine] - cycle)

    df["RUL"] = rul

    X = df.iloc[:, 2:-1].values
    y = df["RUL"].values

    return X, y