const { GalacticRouter } = require('./GalacticRouter');
const Web3 = require('web3');

class GalacticRouter {
    constructor(routerAddress, web3) {
        this.routerAddress = routerAddress;
        this.web3 = web3;
        this.contract = new web3.eth.Contract(GalacticRouter.abi, routerAddress);
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
}

module.exports = GalacticRouter;
