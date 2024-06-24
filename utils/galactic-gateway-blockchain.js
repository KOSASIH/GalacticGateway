// galactic-gateway-blockchain.js
import { GalacticGatewayBlock } from './galactic-gateway-block';

export class GalacticGatewayBlockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock() {
    return new GalacticGatewayBlock([], '0');
  }

  addBlock(block) {
    block.previousBlockHash = this.chain[this.chain.length - 1].getBlockHash();
    this.chain.push(block);
  }

  getBlockchain() {
    return this.chain;
  }
}
