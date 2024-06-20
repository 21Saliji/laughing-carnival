import unittest
from string_cipher import encrypt, decrypt

class CaesarCipherTests(unittest.TestCase):

    def test_basic_encryption_decryption(self):
        message = "hello"
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message)

    def test_longer_message(self):
        message = "thisisalongertestmessage"
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message)

    def test_empty_message(self):
        message = ""
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message)

    def test_message_with_spaces(self):
        message = "hello world"
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message)

    def test_message_with_special_characters(self):
        message = "hello!@#$%"
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, "hello")

    def test_different_key_length(self):
        message = "hello"
        key = "key"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message)

    def test_uppercase_message(self):
        message = "HELLO"
        key = "python"
        encrypted_text = encrypt(message, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, message.lower())

if __name__ == "__main__":
    unittest.main()
