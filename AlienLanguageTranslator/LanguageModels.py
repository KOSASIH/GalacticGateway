import torch
import torch.nn as nn
from transformers import AutoModelForSequenceClassification, AutoConfig

class LanguageModels:
    def __init__(self):
        self.models = {}

    def get_model(self, model_name: str):
        if model_name not in self.models:
            config = AutoConfig.from_pretrained(model_name)
            model = AutoModelForSequenceClassification.from_pretrained(model_name, config=config)
            self.models[model_name] = model
        return self.models[model_name]

    def add_model(self, model_name: str, model: nn.Module):
        self.models[model_name] = model

    def load_trained_model(self, model_name: str, path: str):
        model = self.get_model(model_name)
        model.load_state_dict(torch.load(path, map_location=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')))
        return model
