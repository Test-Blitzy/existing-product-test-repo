const express = require('express');

const hostname = '127.0.0.1';
const port = 3000;
const app = express();

// Root path handler
app.get('/', (req, res) => {
  res.status(200).type('text/plain').send('Hello, World!\n');
});

// Evening path handler
app.get('/evening', (req, res) => {
  res.status(200).type('text/plain').send('Good evening');
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
