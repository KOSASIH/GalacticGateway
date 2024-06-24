const { GalacticNode } = require('./GalacticNode');
const Web3 = require('web3');

class GalacticNode {
    constructor(nodeAddress, web3) {
        this.nodeAddress = nodeAddress;
        this.web3 = web3;
        this.contract = new web3.eth.Contract(GalacticNode.abi, nodeAddress);
    }

    async getNodeInfo() {
        return this.contract.methods.getNodeInfo().call();
    }
}

module.exports = GalacticNode;
