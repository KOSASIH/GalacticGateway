const { GalacticGateway, GalacticToken } = require('./GalacticGateway');
const Web3 = require('web3');

const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

const galacticGateway = new GalacticGateway(web3);
const galacticToken = new GalacticToken(web3);

module.exports = { galacticGateway, galacticToken };
