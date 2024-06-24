// galactic-gateway-transaction.js
export class GalacticGatewayTransaction {
  constructor(from, to, amount, data) {
    this.from = from;
    this.to = to;
    this.amount = amount;
    this.data = data;
  }

  getTransactionHash() {
    return crypto.createHash('sha256').update(JSON.stringify(this)).digest('hex');
  }

  getTransactionSignature(wallet) {
    return wallet.signTransaction(this);
  }
}
