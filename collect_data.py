import pandas as pd

df = pd.read_csv("articles_1.csv", usecols= ["title", "content", "publication"])

for idx, row in enumerate(df.itertuples()):
    if row.publication == "New York Times":
        df.at[idx, "title"] = row.title.replace(f"- The New York Times", "")
    else:
        df.at[idx, "title"] = row.title.replace(f"- {row.publication}", "")

df.drop("publication", inplace=True, axis=1)
df.to_csv("title_article")