import torch
importtorch.nn as nn
from torchvision import models

class GalacticObjectDetector(nn.Module):
    def __init__(self, num_classes):
        super(GalacticObjectDetector, self).__init__()
        self.yolo = models.detection.yolo.YOLO(num_classes)

    def forward(self, image):
        outputs = self.yolo(image)
        return outputs
