from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
  <title>AI FIXORIUM AI</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>FIXORIUM AI</h1>
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
      const response = await fetch('/generate', {
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

@app.route('/', methods=['GET'])
def index():
    return render_template_string(html_template)

@app.route('/generate', methods=['POST'])
def generate_text():
    # Your text generation code here
    return jsonify({'text': 'Generated text'})

if __name__ == '__main__':
    app.run(debug=True)
