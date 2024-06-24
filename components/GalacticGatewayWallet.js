// GalacticGatewayWallet.js
import React, { useState } from 'react';
import { GalacticGatewayWallet } from '../utils/galactic-gateway-wallet';

const GalacticGatewayWallet = () => {
  const [privateKey, setPrivateKey] = useState('');
  const [publicKey, setPublicKey] = useState('');
  const [accountAddress, setAccountAddress] = useState('');

  const handleGenerateWallet = () => {
    const wallet = new GalacticGatewayWallet(privateKey);
    setPublicKey(wallet.getPublicKey());
    setAccountAddress(wallet.getAccountAddress());
  };

  return (
    <div>
      <h1>Galactic Gateway Wallet</h1>
      <input
        type="text"
        value={privateKey}
        onChange={e => setPrivateKey(e.target.value)}
        placeholder="Enter private key"
      />
      <button onClick={handleGenerateWallet}>Generate Wallet</button>
      <p>Public Key: {publicKey}</p>
      <p>Account Address: {accountAddress}</p>
    </div>
  );
};

export default GalacticGatewayWallet;
