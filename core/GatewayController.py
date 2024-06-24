import asyncio
from galactic_network import GalacticNetwork
from data_encryption import DataEncryption

class GatewayController:
    def __init__(self, galactic_network: GalacticNetwork, data_encryption: DataEncryption):
        self.galactic_network = galactic_network
        self.data_encryption = data_encryption

    async def establish_connection(self, alien_ship: str) -> bool:
        # Establish a secure connection with the alien ship
        encrypted_data = self.data_encryption.encrypt("Hello, Galactic Gateway!")
        response = await self.galactic_network.send_data(alien_ship, encrypted_data)
        return response == "Connection established!"

    async def translate_alien_language(self, alien_text: str) -> str:
        # Translate alien language using advanced language models
        translator = AlienLanguageTranslator()
        translated_text = translator.translate(alien_text)
        return translated_text
