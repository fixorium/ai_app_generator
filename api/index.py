import json

def handler(event, context):
    if event['request']['method'] == 'GET':
        return {
            'statusCode': 200,
            'body': """
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
                  const response = await fetch('/', {
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
            """,
            'headers': {
                'Content-Type': 'text/html'
            }
        }
    elif event['request']['method'] == 'POST':
        body = event['request']['body']
        import json
        data = json.loads(body)
        prompt = data['prompt']
        generated_text = f"Generated text for {prompt}"
        return {
            'statusCode': 200,
            'body': json.dumps({'text': generated_text}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
