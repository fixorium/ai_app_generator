// api/index.js
const http = require('http');

module.exports = async function handler(req, res) {
  res.status(200).send('Hello, World!');
};
