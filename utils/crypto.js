// crypto.js
import { CRYPTO_ALGORITHM, CRYPTO_PASSWORD } from './constants';

const crypto = require('crypto');

export function encrypt(data) {
  const cipher = crypto.createCipher(CRYPTO_ALGORITHM, CRYPTO_PASSWORD);
  let encrypted = cipher.update(data, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

export function decrypt(encrypted) {
  const decipher = crypto.createDecipher(CRYPTO_ALGORITHM, CRYPTO_PASSWORD);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}
