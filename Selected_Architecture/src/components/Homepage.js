import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Homepage.css'; // Import the CSS file for styling
import logo from './Flameburger-logo.png'; // Import the image

function Homepage() {
  const [authenticated, setAuthenticated] = useState(false);

  // Function to handle sign out
  const handleSignOut = () => {
    setAuthenticated(false);
  };

  return (
    <div className="homepage-container">
      <header className="header">
        <h1 className="main-heading">Welcome to FlameBurger</h1>
        <p className="description">Discover our delicious burgers, fries, and more!</p>
      </header>

      <section className="content">
        <div className="action-buttons">
          {authenticated ? (
            <button onClick={handleSignOut} className="btn btn-signout">
              Sign Out
            </button>
          ) : (
            <>
              <Link to="/login" className="btn btn-login">
                Login
              </Link>
              <Link to="/register" className="btn btn-register">
                Register
              </Link>
            </>
          )}
        </div>
      </section>

      <div className="brand-logo">
        <img src={logo} alt="FlameBurger Logo" />
      </div>
    </div>
  );
}

export default Homepage;
