 from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    # Your text generation code here
    return jsonify({'text': 'Generated text'})

if __name__ == '__main__':
    app.run(debug=True)
