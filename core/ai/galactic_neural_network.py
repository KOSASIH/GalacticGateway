import torch
import torch.nn as nn
import torch.nn.functional as F

class GalacticNeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GalacticNeuralNetwork, self).__init__()
        self.transformer = TransformerXL(input_dim, hidden_dim, output_dim)
        self.switch_transformer = SwitchTransformer(input_dim, hidden_dim, output_dim)

    def forward(self, x):
        x = self.transformer(x)
        x = self.switch_transformer(x)
        return x
