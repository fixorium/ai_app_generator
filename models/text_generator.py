 import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class TextGenerator:
    def __init__(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")

    def generate_text(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
