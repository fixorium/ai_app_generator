from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>AI App Generator</title>
      <style>
        body {
          font-family: Arial, sans-serif;
        }
      </style>
    </head>
    <body>
      <h1>AI App Generator</h1>
      <form id="generate-form">
        <label for="prompt">Enter a prompt:</label>
        <input type="text" id="prompt" name="prompt">
        <button type="submit">Generate Text</button>
      </form>
      <div id="generated-text"></div>

      <script>
        const form = document.getElementById('generate-form');
        form.addEventListener('submit', async (e) => {
          e.preventDefault();
          const prompt = document.getElementById('prompt').value;
          const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
          });
          const data = await response.json();
          document.getElementById('generated-text').innerText = data.text;
        });
      </script>
    </body>
    </html>
    """

@app.route('/api/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']
    # Your AI model logic here
    generated_text = f"Generated text for {prompt}"
    return jsonify({'text': generated_text})
