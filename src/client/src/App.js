import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);
  
  const premade_data = {
    "pm2.5": 8.0,
    "o3": 57.0,
    "no2": 25.0,
    "temps": 11.3
  }

    fetch('http://localhost:5000/air/predict/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(premade_data)
    })
      .then(response => response.json())
      .then(data => setData(data.predict))
      .catch(error => console.error(error));
  
  return (
    <div>
      <h1>Pridobivanje napovedi s API</h1>
      <p>Model je napovedal da bo vrednost pm10 ob danih pogojih: {data}</p>
    </div>
  );
}

export default App;
