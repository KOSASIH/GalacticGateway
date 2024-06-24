// galactic-gateway-api.js
import axios from 'axios';

const API_URL = 'https://api.galacticgateway.com';

export function getGalacticGatewayData() {
  return axios.get(`${API_URL}/data`);
}

export function getGalacticGatewayNetwork() {
  return axios.get(`${API_URL}/network`);
}

export function getGalacticGatewayChainId() {
  return axios.get(`${API_URL}/chain-id`);
}

export function sendGalacticGatewayTransaction(transaction) {
  return axios.post(`${API_URL}/transaction`, transaction);
}
