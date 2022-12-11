import torch.nn as nn
import torch
from transformers import RobertaModel, RobertaTokenizer


class MyModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.roberta = RobertaModel.from_pretrained("roberta-base")
        self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

    def encoding(self, text):
        tokens = self.tokenizer(text, return_tensors = "pt")
        output = self.roberta(**tokens, output_hidden_states=True)

        hidden_layers = output[2]

        summed_last_4_layers = torch.stack(hidden_layers[-4:]).sum(0)
        print(summed_last_4_layers.shape)

if __name__ == "__main__":
    MyModel().encoding("hi i hate my boyfriend")