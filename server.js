// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

// Create an Express application
const app = express();

// Configure middleware to parse JSON in the request body
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Create a MySQL connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '@Phoenix1365',
  database: 'upcycledb',
});

// Connect to MySQL
db.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL: ' + err.stack);
    return;
  }
  console.log('Connected to MySQL as id ' + db.threadId);
});

// Example route to handle GET requests
app.get('/', (req, res) => {
  res.send('Hello, this is your Node.js server!');
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});


const bcrypt = require('bcrypt');

// ...

// Handle sign-up request
app.post('/signup', async (req, res) => {
  const { full_name, username, birthday, email, password } = req.body;

  const hashedPassword = await bcrypt.hash(password, 10);

  const sql = 'INSERT INTO users (full_name, username, birthday, email, password) VALUES (?, ?, ?, ?, ?)';
  db.query(sql, [full_name, username, birthday, email, hashedPassword], (err, result) => {
    if (err) {
      console.error('Error executing MySQL query: ' + err.stack);
      res.status(500).send('Error signing up');
      return;
    }
    console.log('User signed up successfully');
    res.status(200).send('Registration complete!');
  });
});

// ...

// Handle login request
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  const sql = 'SELECT * FROM users WHERE email = ?';
  db.query(sql, [email], async (err, result) => {
    if (err) {
      console.error('Error executing MySQL query: ' + err.stack);
      res.status(500).send('Error during login');
      return;
    }

    if (result.length > 0) {
      const hashedPassword = result[0].password;
      const passwordMatch = await bcrypt.compare(password, hashedPassword);

      if (passwordMatch) {
        console.log('Login successful');
        res.status(200).send('Login successful');
      } else {
        console.log('Invalid email or password');
        res.status(401).send('Invalid email or password');
      }
    } else {
      console.log('Invalid email or password');
      res.status(401).send('Invalid email or password');
    }
  });
});