import pandas as pd
from transformers import RobertaTokenizer
import tensorflow as tf


def load_data(path: str, split=0.8):
    df = pd.read_csv(path, index_col=0)
    size = len(df)
    train_ds = df[:round(size*split)]
    test_ds = df[round(size*split):]
    return train_ds, test_ds
