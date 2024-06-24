// galactic-gateway-wallet.js
import { encrypt, decrypt } from './crypto';

export class GalacticGatewayWallet {
  constructor(privateKey) {
    this.privateKey = privateKey;
  }

  getPublicKey() {
    return encrypt(this.privateKey, 'public-key');
  }

  getAccountAddress() {
    return encrypt(this.privateKey, 'account-address');
  }

  signTransaction(transaction) {
    return encrypt(transaction, this.privateKey);
  }

  verifyTransaction(transaction, signature) {
    return decrypt(signature, this.privateKey) === transaction;
  }
}
