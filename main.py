from dataloader import load_data
import pandas as pd

path = path = r"dataset\small_title_article.csv"

train_ds, test_ds = load_data(path)
print(train_ds)