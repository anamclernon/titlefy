import pandas as pd
from transformers import RobertaTokenizer


class DataLoader:
    def __init__(self, file_path: str) -> None:
        self.dataset = pd.read_csv(path, index_col=0)
        self.features = self.dataset["content"]
        self.labels = self.dataset["title"]

    def __len__(self):
        return len(self.dataset)

    def split_data(self, split=0.8) -> tuple[pd.DataFrame]:
        train_features = self.features[round(len(self)) :]
        train_labels = self.labels[round(len(self)) :]
        test_features = self.features[: round(len(self))]
        test_labels = self.labels[: round(len(self))]
        return train_features, train_labels, test_features, test_labels


if __name__ == "__main__":
    path = r"..\titlefy_dataset\small_title_article.csv"
    data = DataLoader(path)
    print(data.dataset)
