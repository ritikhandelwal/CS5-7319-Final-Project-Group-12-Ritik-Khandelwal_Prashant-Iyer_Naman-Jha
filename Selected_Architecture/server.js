  const express = require('express');
  const pg = require('pg');
  const bodyParser = require('body-parser');
  const cors = require('cors');
  const bcrypt = require('bcrypt'); 
  const jwt = require('jsonwebtoken'); 
  require('dotenv').config();
  const crypto = require('crypto');
  const JWT_SECRET_KEY = crypto.randomBytes(32).toString('hex');



  const app = express();
  const port = process.env.PORT || 3000;


  const pool = new pg.Pool({
    user: 'postgres',
    password: 'postgres1',
    host: 'localhost',
    database: 'my_restaurant_db',
    port: 5432,
  });

  app.use(cors());
  app.use(bodyParser.json());


  app.get('/user', async (req, res) => {
    const { username } = req.query;
    try {
      const client = await pool.connect();
      const result = await client.query('SELECT id FROM users WHERE username = $1', [username]);
      if (result.rows.length > 0) {
        const userId = result.rows[0].id;
        res.json({ userId });
      } else {
        res.status(404).json({ message: 'User not found' });
      }
      await client.release();
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });


  // Route to handle user registration
  app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    try {
      const hashedPassword = await bcrypt.hash(password, 10); // 10 is the saltRounds parameter, increasing it increases the security but also the computation time

      // Insert the user into the database with the hashed password
      const client = await pool.connect();
      const insertQuery = 'INSERT INTO users (username, password_hash) VALUES ($1, $2) RETURNING *';
      const values = [username, hashedPassword];
      const result = await client.query(insertQuery, values);

      if (result.rows.length > 0) {
        const user = result.rows[0];
        res.json({ message: 'User registered successfully!', user });
      } else {
        res.status(500).json({ message: 'Failed to register user' });
      }
      await client.release();
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });


  // Route to handle user login
  app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
      const client = await pool.connect();
      const result = await client.query('SELECT * FROM users WHERE username = $1', [username]);
      if (result.rows.length > 0) {
        const user = result.rows[0];
        const passwordMatch = await bcrypt.compare(password, user.password_hash);
        if (passwordMatch) {
          const token = jwt.sign({ userId: user.id }, JWT_SECRET_KEY, { expiresIn: '1h' });
          res.json({ message: 'Login successful!', token });
        } else {
          res.status(401).json({ message: 'Invalid username or password' });
        }
      } else {
        res.status(401).json({ message: 'Invalid username or password' });
      }
      await client.release();
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });

  //Get Menu
  app.get('/menu', async (req, res) => {
    try {
      const client = await pool.connect();
      const result = await client.query('SELECT * FROM menu_items');
      const menuItems = result.rows;
      res.json(menuItems);
      await client.release();
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });
  
// Route to handle placing orders
app.post('/orders', async (req, res) => {
  const { username, items } = req.body;

  // Validate username and items presence
  if (!username || !items || items.length === 0) {
    return res.status(400).json({ message: 'Missing required order details' });
  }

  try {
    const client = await pool.connect();
    const menuQuery = await client.query('SELECT name FROM menu_items');
    const menuItems = menuQuery.rows.map(row => row.name);

    for (const item of items) {
      if (!menuItems.includes(item.name)) {
        return res.status(400).json({ message: `Item '${item.name}' is not available in the menu` });
      }
    }

    let totalPrice = 0;
    for (const item of items) {
      totalPrice += item.quantity * item.price;
    }

    const insertQuery = 'INSERT INTO orders (username, items, total_price) VALUES ($1, $2, $3) RETURNING *';
    const values = [username, JSON.stringify(items), totalPrice];
    const result = await pool.query(insertQuery, values);

    if (result.rows.length > 0) {
      const order = result.rows[0];
      res.json({ message: 'Order placed successfully!', order });
    } else {
      res.status(500).json({ message: 'Failed to place order' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});


  app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
  });
