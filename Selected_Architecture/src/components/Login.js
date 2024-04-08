// Login.js
import React, { useState } from 'react';
import LoginForm from './LoginForm'; // Import the LoginForm component
import Menu from './Menu'; // Import the Menu component

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [loggedIn, setLoggedIn] = useState(false); // Add loggedIn state

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('Submitting login request...');
  
    try {
      const response = await fetch('http://localhost:3000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
      });
  
      console.log('Response:', response);
  
      const data = await response.json();
      console.log('Data received:', data);
  
      if (response.ok) {
        localStorage.setItem('token', data.token);
        setMessage('Login successful!');
        setLoggedIn(true); // Set loggedIn to true upon successful login
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred. Please try again later.');
    }
  };
  sessionStorage.setItem('username', username);


  return (
    <div>
      {loggedIn ? (
        <Menu /> // If logged in, render the Menu component
      ) : (
        <LoginForm
          username={username}
          setUsername={setUsername}
          password={password}
          setPassword={setPassword}
          handleSubmit={handleSubmit}
          message={message}
        />
      )}
    </div>
  );
}

export default Login;
