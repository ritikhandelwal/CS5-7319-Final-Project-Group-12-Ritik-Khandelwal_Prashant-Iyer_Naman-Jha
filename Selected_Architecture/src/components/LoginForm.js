import React from 'react';
import './LoginForm.css'; // Import the LoginForm css

function LoginForm({ username, setUsername, password, setPassword, handleSubmit, message }) {
  return (
    <div className="login-container">
      <div className="flame-burger-section">
        <h1>FlameBurger</h1> 
      </div>
      <div className="login-form">
        {/* Your login text, username and password input boxes */}
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">Login</button>
        </form>
        {message && <div className="error-message">{message}</div>}
      </div>
    </div>
  );
}

export default LoginForm;
