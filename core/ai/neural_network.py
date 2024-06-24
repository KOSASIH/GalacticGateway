# galactic_gateway/core/ai/neural_network.py
import torch
import torch.nn as nn
import torch.optim as optim

class GalacticNeuralNetwork(nn.Module):
    def __init__(self):
        super(GalacticNeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(1024, 512)  # Input layer (1024) -> Hidden layer (512)
        self.fc2 = nn.Linear(512, 256)  # Hidden layer (512) -> Hidden layer (256)
        self.fc3 = nn.Linear(256, 128)  # Hidden layer (256) -> Output layer (128)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Activation function for hidden layer
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = GalacticNeuralNetwork()
