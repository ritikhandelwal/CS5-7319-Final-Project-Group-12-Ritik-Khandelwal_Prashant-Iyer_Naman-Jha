import React, { useState, useEffect } from 'react';
import './Menu.css';

function Menu() {
  const getUsername = () => {
    const username = sessionStorage.getItem('username');
    return username;
  };

  const [menuItems, setMenuItems] = useState([]);
  const [basketItems, setBasketItems] = useState([]);
  const [totalCost, setTotalCost] = useState(0);
  const [orderStatus, setOrderStatus] = useState(null);
  const [currentOrder, setCurrentOrder] = useState([]); // State for current order

  useEffect(() => {
    fetchMenuItems();
  }, []);

  const fetchMenuItems = async () => {
    try {
      const response = await fetch('http://localhost:3000/menu');
      if (response.ok) {
        const data = await response.json();
        setMenuItems(data);
      } else {
        console.error('Failed to fetch menu items');
      }
    } catch (error) {
      console.error('Error fetching menu items:', error);
    }
  };

  const addToBasket = (item) => {
    const updatedBasket = [...basketItems];
    const existingItemIndex = updatedBasket.findIndex((basketItem) => basketItem.id === item.id);
    if (existingItemIndex !== -1) {
      updatedBasket[existingItemIndex].quantity++;
    } else {
      updatedBasket.push({ ...item, quantity: 1 });
    }
    setBasketItems(updatedBasket);
    calculateTotalCost(updatedBasket);
  };

  const removeFromBasket = (itemId) => {
    const updatedBasket = basketItems.filter((item) => item.id !== itemId);
    setBasketItems(updatedBasket);
    calculateTotalCost(updatedBasket);
  };

  const calculateTotalCost = (items) => {
    let cost = 0;
    items.forEach((item) => {
      cost += item.price * item.quantity;
    });
    setTotalCost(cost);
  };

  const placeOrder = async () => {
    const username = getUsername();
    try {
      const response = await fetch('http://localhost:3000/orders', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username, items: basketItems }),
      });
      if (response.ok) {
        setOrderStatus('success');
        setCurrentOrder([...basketItems]); // Store current order
        setBasketItems([]);
        setTotalCost(0);
      } else {
        console.error('Failed to place order');
      }
    } catch (error) {
      console.error('Error placing order:', error);
    }
  };

  const returnToHomepage = () => {
    window.location.href = '/';
  };

  return (
    <div className="menu-container">
      <div className="menu-heading">
        <h2>Menu</h2>
      </div>
      <div className="menu-table-basket-container">
        <div className="menu-table-container">
          <table className="menu-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {menuItems.map((item) => (
                <tr key={item.id} className="menu-item">
                  <td>{item.name}</td>
                  <td>${item.price}</td>
                  <td>
                    <button onClick={() => addToBasket(item)}>+</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="basket-container">
          <h3>Basket</h3>
          <ul className="basket-list">
            {basketItems.map((item) => (
              <li key={item.id} className="basket-item">
                <div className="basket-item-details">
                  <span>{item.name}</span>
                  <span className="basket-item-price">${item.price} x {item.quantity}</span>
                </div>
                <button onClick={() => removeFromBasket(item.id)}>Remove</button>
              </li>
            ))}
          </ul>
          <p>Total Cost: ${totalCost}</p>
          <button onClick={placeOrder}>Place Order</button>
          {orderStatus === 'success' && (
            <div className="order-success-message">
              <p>Order placed successfully!</p>
              <div className="current-order">
                <h3>Current Order</h3>
                <ul>
                  {currentOrder.map((item) => (
                    <li key={item.id} className="current-order-item">
                      <div>
                        <span>{item.name}</span>
                        <span className="current-order-item-price">${item.price} x {item.quantity}</span>
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
              <button onClick={returnToHomepage}>Sign Out</button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Menu;
