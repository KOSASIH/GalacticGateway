// galactic-gateway-block.js
export class GalacticGatewayBlock {
  constructor(transactions, previousBlockHash) {
    this.transactions = transactions;
    this.previousBlockHash = previousBlockHash;
  }

  getBlockHash() {
    return crypto.createHash('sha256').update(JSON.stringify(this)).digest('hex');
  }
}
