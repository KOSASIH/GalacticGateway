const { GalacticBridge } = require('./GalacticBridge');
const Web3 = require('web3');

class GalacticBridge {
    constructor(bridgeAddress, web3) {
        this.bridgeAddress = bridgeAddress;
        this.web3 = web3;
        this.contract = new web3.eth.Contract(GalacticBridge.abi, bridgeAddress);
    }

    async addNode(nodeAddress, nodeType) {
        return this.contract.methods.addNode(nodeAddress, nodeType).send({ from: this.web3.eth.accounts[0] });
    }

    async removeNode(nodeAddress) {
        return this.contract.methods.removeNode(nodeAddress).send({ from: this.web3.eth.accounts[0] });
    }

    async getNode(nodeAddress) {
        return this.contract.methods.getNode(nodeAddress).call();
    }

    async transferTokens(from, to, amount) {
        return this.contract.methods.transferTokens(from, to, amount).send({ from: this.web3.eth.accounts[0] });
    }
}

module.exports = GalacticBridge;
