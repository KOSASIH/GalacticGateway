const { GalacticOracle } = require('./GalacticOracle');
const Web3 = require('web3');

class GalacticOracle {
    constructor(oracleAddress, web3) {
        this.oracleAddress = oracleAddress;
        this.web3 = web3;
        this.contract = new web3.eth.Contract(GalacticOracle.abi, oracleAddress);
    }

    async updateNodeData(node, data) {
        return this.contract.methods.updateNodeData(node, data).send({ from: this.web3.eth.accounts[0] });
    }

    async getNodeData(node) {
        return this.contract.methods.getNodeData(node).call();
    }
}

module.exports = GalacticOracle;
