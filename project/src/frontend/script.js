document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('root');
    root.innerHTML = `
        <h1>AI Content Generator</h1>
        <textarea id="prompt" placeholder="Enter your prompt here..."></textarea>
        <button id="generate-btn">Generate</button>
        <div id="response-container">
            <h3>Generated Response:</h3>
            <div id="response"></div>
        </div>
    `;

    const generateBtn = document.getElementById('generate-btn');
    const promptInput = document.getElementById('prompt');
    const responseDiv = document.getElementById('response');

    generateBtn.addEventListener('click', async () => {
        const prompt = promptInput.value;
        if (!prompt) {
            alert('Please enter a prompt.');
            return;
        }

        responseDiv.textContent = 'Generating...';

        try {
            const response = await fetch('http://localhost:3000/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            responseDiv.textContent = data.response;
        } catch (error) {
            console.error('Error:', error);
            responseDiv.textContent = 'Failed to generate response. Check the console for details.';
        }
    });
});
