import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from LanguageModels import LanguageModels

class AlienLanguageTranslator:
    def __init__(self, language_models: LanguageModels):
        self.language_models = language_models
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def translate(self, alien_text: str) -> str:
        # Load the alien language model
        model_name = "GalacticTransformerXL"
        model = self.language_models.get_model(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Preprocess the alien text
        inputs = tokenizer.encode_plus(
            alien_text,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors='pt'
        )

        # Move inputs to the device (GPU or CPU)
        inputs['input_ids'] = inputs['input_ids'].to(self.device)
        inputs['attention_mask'] = inputs['attention_mask'].to(self.device)

        # Translate the alien text using the model
        outputs = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
        logits = outputs.logits
        translated_text = torch.argmax(logits, dim=1)

        # Postprocess the translated text
        translated_text = tokenizer.decode(translated_text, skip_special_tokens=True)
        return translated_text

    def train_model(self, alien_text_data: list, human_text_data: list):
        # Train the alien language model
        model_name = "GalacticTransformerXL"
        model = self.language_models.get_model(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Create a custom dataset class for the alien language data
        class AlienLanguageDataset(torch.utils.data.Dataset):
            def __init__(self, alien_text_data, human_text_data):
                self.alien_text_data = alien_text_data
                self.human_text_data = human_text_data

            def __len__(self):
                return len(self.alien_text_data)

            def __getitem__(self, idx):
                alien_text = self.alien_text_data[idx]
                human_text = self.human_text_data[idx]

                inputs = tokenizer.encode_plus(
                    alien_text,
                    add_special_tokens=True,
                    max_length=512,
                    return_attention_mask=True,
                    return_tensors='pt'
                )

                labels = tokenizer.encode_plus(
                    human_text,
                    add_special_tokens=True,
                    max_length=512,
                    return_attention_mask=True,
                    return_tensors='pt'
                )

                return {
                    'input_ids': inputs['input_ids'].flatten(),
                    'attention_mask': inputs['attention_mask'].flatten(),
                    'labels': labels['input_ids'].flatten()
                }

        # Create a data loader for the dataset
        dataset = AlienLanguageDataset(alien_text_data, human_text_data)
        data_loader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

        # Train the model
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=1e-5)

        for epoch in range(10):
            model.train()
            total_loss = 0
            for batch in data_loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                optimizer.zero_grad()

                outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = criterion(outputs, labels)

                loss.backward()
                optimizer.step()

                total_loss += loss.item()

            print(f'Epoch {epoch+1}, Loss: {total_loss / len(data_loader)}')

        model.eval()
        torch.save(model.state_dict(), f'{model_name}_trained.pth')
