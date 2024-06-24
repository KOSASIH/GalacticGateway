// storage.js
import { STORAGE_LOCAL, STORAGE_SESSION } from './constants';

export function setLocalStorage(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}

export function getLocalStorage(key) {
  const value = localStorage.getItem(key);
  return value? JSON.parse(value) : null;
}

export function removeLocalStorage(key) {
  localStorage.removeItem(key);
}

export function setSessionStorage(key, value) {
  sessionStorage.setItem(key, JSON.stringify(value));
}

export function getSessionStorage(key) {
  const value = sessionStorage.getItem(key);
  return value? JSON.parse(value) : null;
}

export function removeSessionStorage(key) {
  sessionStorage.removeItem(key);
}
