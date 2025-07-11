 from flask import Flask, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

model_name = "t5-small"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get("prompt", "")
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({"text": generated_text})

if __name__ == '__main__':
    app.run(debug=True)
