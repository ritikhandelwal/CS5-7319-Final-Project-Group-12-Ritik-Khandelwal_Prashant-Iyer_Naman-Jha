// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import Routes from react-router-dom

// Import your components here
import Homepage from './components/Homepage';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
    <Router>
      {/* Use Routes instead of Switch */}
      <Routes>
        <Route exact path="/" element={<Homepage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
