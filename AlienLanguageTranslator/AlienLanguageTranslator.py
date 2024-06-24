import torch
from language_models import LanguageModels

class AlienLanguageTranslator:
    def __init__(self, language_models: LanguageModels):
        self.language_models = language_models

    def translate(self, alien_text: str) -> str:
        # Translate alien language using deep learning models
        model = self.language_models.get_model("AlienLanguageModel")
        translated_text = model.translate(alien_text)
        return translated_text
