// GalacticGatewayDashboard.js
import React, { useState, useEffect } from 'react';
import { getGalacticGatewayData } from '../utils/galactic-gateway-api';

const GalacticGatewayDashboard = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    getGalacticGatewayData().then(response => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Galactic Gateway Dashboard</h1>
      <p>Data: {JSON.stringify(data)}</p>
    </div>
  );
};

export default GalacticGatewayDashboard;
