import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [model, setModel] = useState('text-generator');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [appType, setAppType] = useState('web');
  const [template, setTemplate] = useState('basic');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('/api/generate', { input, model, appType, template });
      setOutput(response.data);
      setError(null);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <select value={appType} onChange={(e) => setAppType(e.target.value)}>
          <option value="web">Web App</option>
          <option value="mobile">Mobile App</option>
          <option value="desktop">Desktop App</option>
        </select>
        <select value={template} onChange={(e) => setTemplate(e.target.value)}>
          <option value="basic">Basic Template</option>
          <option value="advanced">Advanced Template</option>
        </select>
        <select value={model} onChange={(e) => setModel(e.target.value)}>
          <option value="text-generator">Text Generator</option>
          <option value="image-generator">Image Generator</option>
          <option value="music-generator">Music Generator</option>
        </select>
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
        <button type="submit" disabled={loading}>
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </form>
      {output && <div>Output: {output}</div>}
      {error && <div style={{ color: 'red' }}>Error: {error}</div>}
    </div>
  );
}

export default App;
