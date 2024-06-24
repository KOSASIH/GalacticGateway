# galactic_pattern_recognition.py
import torch
import torch.nn as nn
import torch.optim as optim

class GalacticPatternRecognition(nn.Module):
    def __init__(self):
        super(GalacticPatternRecognition, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv3 = nn.Conv2d(20, 30, kernel_size=5)
        self.fc1 = nn.Linear(30*5*5, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = x.view(-1, 30*5*5)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = GalacticPatternRecognition()
