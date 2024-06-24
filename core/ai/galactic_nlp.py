import torch
import torch.nn as nn
from transformers import BertTokenizer, BertModel

class GalacticNLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GalacticNLP, self).__init__()
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.bert_model = BertModel.from_pretrained('bert-base-uncased')
        self.graph_sage = GraphSAGE(input_dim, hidden_dim, output_dim)

    def forward(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        attention_mask = self.tokenizer.encode(input_text, return_tensors='pt', max_length=512, padding='max_length', truncation=True)
        outputs = self.bert_model(input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        graph_output = self.graph_sage(pooled_output)
        return graph_output
