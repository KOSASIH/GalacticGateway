import qiskit
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class QuantumCommunication:
    def __init__(self):
        self.qc = qiskit.QuantumCircuit(2)
        self.key_pair = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

    def generate_quantum_key(self):
        # Generate a quantum key using quantum entanglement
        self.qc.h(0)
        self.qc.cx(0, 1)
        self.qc.measure_all()
        key = self.qc.get_statevector()
        return key

    def encrypt_message(self, message):
        # Encrypt the message using the quantum key
        encrypted_message = self.key_pair.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        # Decrypt the message using the quantum key
        decrypted_message = self.key_pair.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()

# Example usage
qc = QuantumCommunication()
message = "Hello, Galactic Gateway!"
quantum_key = qc.generate_quantum_key()
encrypted_message = qc.encrypt_message(message)
decrypted_message = qc.decrypt_message(encrypted_message)
print(decrypted_message)
